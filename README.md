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
   git clone [https://github.com/YourUsername/ros2_edge_camera_boilerplate.git](https://github.com/YourUsername/ros2_edge_camera_boilerplate.git)
