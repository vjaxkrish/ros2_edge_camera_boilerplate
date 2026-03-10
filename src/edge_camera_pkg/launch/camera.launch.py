from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    camera_id_arg = DeclareLaunchArgument(
        'camera_id', default_value='0',
        description='ID of the camera (e.g., 0 for USB, or CSI sensor ID)'
    )
    
    use_gst_arg = DeclareLaunchArgument(
        'use_gst', default_value='False',
        description='Set to True to use GStreamer pipeline for Jetson CSI cameras'
    )
    
    fps_arg = DeclareLaunchArgument(
        'fps', default_value='30',
        description='Target framerate for the camera'
    )

    camera_node = Node(
        package='edge_camera_pkg',
        executable='camera_node',
        name='edge_camera_node',
        output='screen',
        parameters=[{
            'camera_id': LaunchConfiguration('camera_id'),
            'use_gst': LaunchConfiguration('use_gst'),
            'fps': LaunchConfiguration('fps')
        }]
    )

    return LaunchDescription([
        camera_id_arg,
        use_gst_arg,
        fps_arg,
        camera_node
    ])
