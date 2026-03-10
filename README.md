# ROS2 Edge Camera Boilerplate

A lightweight, well-documented ROS2 workspace template designed for quick and reliable camera integration on edge devices. It supports standard USB webcams and includes a pre-configured GStreamer pipeline for Nvidia Jetson CSI cameras.

## Features
- **Plug-and-Play:** Easily switch between USB `/dev/video*` and CSI cameras.
- **Diagnostics:** Built-in lightweight framerate tracking.
- **Edge Optimized:** Tested on Nvidia Jetson and Raspberry Pi architectures.

## Prerequisites
- ROS2 (Humble / Foxy / Iron / Jazzy)
- OpenCV (`python3-opencv`)
- CV Bridge (`ros-<distro>-cv-bridge`)

## Installation

1. Clone the repository into your workspace:
   ```bash
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws/src
   git clone [https://github.com/vjaxkrish/ros2_edge_camera_boilerplate.git](https://github.com/vjaxkrish/ros2_edge_camera_boilerplate.git)

 2. Build the package:
   ```bash
   cd ~/ros2_ws
   colcon build --packages-select edge_camera_pkg
   source install/setup.bash
```

   ## Usage
   
   You can run the node using the standard `ros2 run` command, or use the included launch file for an easier setup.
   
   **Using the Launch File (Recommended):**
   
   Run with a standard USB Camera (Default):
   ```bash
   ros2 launch edge_camera_pkg camera.launch.py
```

## Run with an Nvidia Jetson CSI Camera:
```bash
ros2 launch edge_camera_pkg camera.launch.py use_gst:='True' camera_id:='0' fps:='30'
```
## Viewing the feed ::
```bash
ros2 run rqt_image_view rqt_image_view
```

      
