import os
import launch
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

from pathlib import Path


def generate_launch_description():

    components = []
    
    components.append(launch.actions.IncludeLaunchDescription(
                    XMLLaunchDescriptionSource(os.path.join(get_package_share_directory("vesc_ackermann"), 'launch', "vesc_to_odom_node.launch.xml")),
                ))

    components.append(launch.actions.IncludeLaunchDescription(
                    XMLLaunchDescriptionSource(os.path.join(get_package_share_directory("vesc_ackermann"), 'launch', "ackermann_to_vesc_node.launch.xml")),
                ))

    components.append(launch.actions.IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("vesc_driver"), 'launch', "vesc_driver_node.launch.py")),
                ))

    return launch.LaunchDescription(components)
