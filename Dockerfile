FROM tiryoh/ros2-desktop-vnc:humble

# Set environment variables
RUN echo "source ~/turtlebot3_ws/install/setup.bash" >> ~/.bashrc
RUN echo "export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/turtlebot3_ws/src/turtlebot3/turtlebot3_simulations/turtlebot3_gazebo/models" >> ~/.bashrc

# Source bashrc to set environment variables
RUN source ~/.bashrc

# Update and upgrade packages
RUN sudo apt update -y && sudo apt upgrade -y

# Install ROS 2 packages for navigation and turtlebot3
RUN sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup ros-humble-turtlebot3* ros-humble-rmw-cyclonedds-cpp \
	ros-humble-nav2-simple-commander ros-humble-tf-transformations python3-transforms3d \
	-y