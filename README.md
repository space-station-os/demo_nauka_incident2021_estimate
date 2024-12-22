# demo_nauka_incident2021_estimate
Demo#1: Estimates of Nauka incident on ISS in July 2021 and more

## Prerequisites
- Ubuntu 22.04
- ROS 2 Humble (desktop install)

## Installation
Common procedures for preparing Space Station OS:
- Install Ubuntu 22.04
- Install ROS 2 Humble (desktop install):
  https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html

- Clone Space Station OS source

    ```sh
    cd /path/to/ros2_ws
    mkdir src
    cd src
    git clone https://github.com/space-station-os/demo_nauka_incident2021_estimate.git
    ```

- Compile Space Station OS source

    ```sh
    cd /path/to/ros2_ws
    colcon build --symlink-install
    source install/setup.bash
    ```

## Demo1: Estimates of Nauka incident on ISS in July 2021 and more
Demo1 focuses on space station GNC features.

In Demo 1a, we estimate what happened and how the system and people reacted in the Nauka incident that occurred on the ISS in July 2021.
https://www.nasaspaceflight.com/2021/07/nauka-docking/
In Demo 1b, we prepared for an imaginary difficult case.

Through these cases, we will study the importance of determining fault detection, isolation and recovery (FDIR).

### Procedures to run Demo 1a/1b
1. Terminal 1: handles scenario description and user input.
    - for Demo 1a
        ```sh
        ros2 run demo_nauka_incident2021_estimate demo1a_nauka_incident_estimate
        ```

    - for Demo 1b
        ```sh
        ros2 run demo_nauka_incident2021_estimate demo1b_crisis_mainengine
        ```

2. Terminal 2: handles space station propulsion system and attitude control dynamics, where the user (you) do not need to touch thereafter.
    - common for Demo 1a/1b
        ```sh
        ros2 launch demo_nauka_incident2021_estimate launch_gnc.py
        ```

3. Terminal 3: Visualization in RViz
    - We use RViz, a common tool for visualization in ROS 2.
    - common for Demo 1a/1b
        ```sh
        ros2 run rviz2 rviz2
        ```
    - Choose `Fixed Frame`, change from `map` to `world`
    - Add a robot visualization : `Add` -> `RobotModel`
    - Choose the  `Description Topic` of the `RobotModel`: use `/robot_description`
    - You should now see the ISS model in rviz (you may need to zoom out)

4. Then you go back to Terminal 1 and follow the scenario in the console as the attitude of ISS is displayed in rviz2.

## TODOs
Moved to project backlog https://github.com/orgs/space-station-os/projects/2/views/1 
