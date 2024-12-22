#!/usr/bin/env python3

from ament_index_python.packages import get_package_share_directory
import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    package_share_directory = get_package_share_directory('demo_nauka_incident2021_estimate')
    urdf_file_path = os.path.join(package_share_directory,'urdf','ISS_stationaryFromNasa.urdf')
    with open(urdf_file_path, 'r') as urdf_file:
        urdf_data = urdf_file.read()
        
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': urdf_data}],
        ),
        Node(
            package='demo_nauka_incident2021_estimate',
            executable='torque_collector',
            name='torque_collector'
        ),
        Node(
            package='demo_nauka_incident2021_estimate',
            executable='attitude_dynamics',
            name='attitude_dynamics'
        )
        
    ])
