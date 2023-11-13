# 2023-2A-T2-M8-P1

This project use the gazebo simulator, with rviz and ros2 to simulate a robot that can move autonomously in a map from waypoints previously defined on [code](https://github.com/ViniciosLugli/2023-2A-T2-M8-P1/blob/9f5b8e7689d2da0277bb9604636c96eae7084ca0/project_ws/controller_package/controller_package/node.py#L37).

## Setup project

The main packages used in this project are the [ros2](https://docs.ros.org/en/humble/index.html), [gazebo](https://classic.gazebosim.org/) and [rviz2](https://github.com/ros2/rviz). To install and use the project, you need a linux distribution, recommended [Ubuntu 22.04 LTS](https://ubuntu.com/download/desktop).

### Install ROS2

To install ROS2, follow the [official documentation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html).
After install ROS2, you need to setup the bash script to use the ROS2 commands, to do this, run the following command:

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

:warning: **Note:** If you use another shell, like zsh, you need to change the file .bashrc to .zshrc.

### Install Rviz2 navigation

To install the rviz2 navigation, follow the commands:

```bash
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup ros-humble-turtlebot3* ros-humble-rmw-cyclonedds-cpp
```

:warning: **Note:** If you use another shell, like zsh, you need to change the `ros-humble-turtlebot3*` to `"ros-humble-turtlebot3*"`.

Export the RMW implementation:

```bash
echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc
```

:warning: **Note:** If you use another shell, like zsh, you need to change the file .bashrc to .zshrc.

### Setup Gazebo

Add this environment variable to your .bashrc/.zshrc file:

```bash
export TURTLEBOT3_MODEL=burger
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models
```

### Install another dependencies

```bash
sudo apt-get install ros-humble-turtle-tf2-py ros-humble-tf2-tools ros-humble-tf-transformations
```

### After install all dependencies

Source the bash script:

```bash
source ~/.bashrc
```

or if you use zsh:

```bash
source ~/.zshrc
```

### Project

Setup the project in your workspace:

#### Clone

Get the project:

```bash
git clone git@github.com:ViniciosLugli/2023-2A-T2-M8-P1.git
```

Go to the project folder:

```bash
cd 2023-2A-T2-M8-P1/project_ws
```

#### Build

Use the colcon to build the project:

```bash
colcon build
```

#### Source

Source the project:

```bash
source install/setup.bash
```

or if you use zsh:

```bash
source install/setup.zsh
```

## Start project manual

### Start gazebo world

Using the turtlebot3 burger world:

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

### Start rviz2

Setup rviz map:

```bash
ros2 launch nav2_bringup bringup_launch.py use_sim_time:=True map:=mapa.yaml
```

Start rviz2 gui:

```bash
ros2 run rviz2 rviz2 -d $(ros2 pkg prefix nav2_bringup)/share/nav2_bringup/rviz/nav2_default_view.rviz
```

### Start controller

To start the controller, run the following command and the robot will move to the waypoints:

```bash
ros2 run controller_package node
```

## Start project using launch

### Mapping

To start mapping the scenario, run the following command:

```bash
ros2 launch controller_package mapping_launch.xml
```

### Navigation

To start the navigation, run the following command:

```bash
ros2 launch controller_package navigation_launch.xml
```

## Demo

### Mapping the scenario

https://github.com/ViniciosLugli/2023-2A-T2-M8-P1/assets/40807526/09ae1de3-7817-4dee-8597-3f963ce10fcc

### Map waypoints

![waypoints](https://github.com/ViniciosLugli/2023-2A-T2-M8-P1/assets/40807526/a086e8bd-8c20-400e-bbe0-84d66d72cf52)

### Video

https://github.com/ViniciosLugli/2023-2A-T2-M8-P1/assets/40807526/cd23cb3b-06d7-4a73-a535-9db6e17a9c58
