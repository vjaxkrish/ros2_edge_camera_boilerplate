import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import time

class EdgeCameraNode(Node):
    def __init__(self):
        super().__init__('edge_camera_node')
        
        # Declare parameters
        self.declare_parameter('camera_id', 0)
        self.declare_parameter('use_gst', False) # Set to True for Jetson CSI cameras
        self.declare_parameter('fps', 30)
        
        camera_id = self.get_parameter('camera_id').value
        use_gst = self.get_parameter('use_gst').value
        self.target_fps = self.get_parameter('fps').value

        # Publisher
        self.publisher_ = self.create_publisher(Image, 'camera/image_raw', 10)
        self.bridge = CvBridge()

        # Initialize VideoCapture
        if use_gst:
            # Standard GStreamer pipeline for Nvidia Jetson CSI cameras
            gst_pipeline = (
                f"nvarguscamerasrc sensor-id={camera_id} ! "
                "video/x-raw(memory:NVMM), width=1280, height=720, format=(string)NV12, framerate=(fraction)30/1 ! "
                "nvvidconv ! video/x-raw, format=(string)BGRx ! "
                "videoconvert ! video/x-raw, format=(string)BGR ! appsink"
            )
            self.cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)
            self.get_logger().info(f"Connecting to CSI Camera {camera_id} via GStreamer...")
        else:
            self.cap = cv2.VideoCapture(camera_id)
            self.get_logger().info(f"Connecting to USB Camera {camera_id}...")

        if not self.cap.isOpened():
            self.get_logger().error("Failed to open camera!")
            return

        # Timer for publishing frames
        timer_period = 1.0 / self.target_fps
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # FPS tracking variables
        self.prev_time = time.time()
        self.frame_count = 0

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warning("Dropped frame!")
            return

        # Convert OpenCV image to ROS2 Image message
        msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        self.publisher_.publish(msg)

        # Calculate and log real FPS every 30 frames
        self.frame_count += 1
        if self.frame_count % 30 == 0:
            current_time = time.time()
            elapsed = current_time - self.prev_time
            actual_fps = 30 / elapsed
            self.get_logger().info(f"Publishing at {actual_fps:.2f} FPS")
            self.prev_time = current_time

    def destroy_node(self):
        self.cap.release()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = EdgeCameraNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
