import os
import launch
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

from pathlib import Path


def generate_launch_description():

    params = {"speed_to_erpm_gain": "4614.0", "speed_to_erpm_offset": "0.0",
              "steering_angle_to_servo_gain": "-1.2135", "steering_angle_to_servo_offset": "0.5304"}

    components = []

    components.append(launch.actions.IncludeLaunchDescription(
        XMLLaunchDescriptionSource(os.path.join(get_package_share_directory(
            "vesc_ackermann"), 'launch', "vesc_to_odom_node.launch.xml")), launch_arguments=params.items(),
    ))

    components.append(launch.actions.IncludeLaunchDescription(
        XMLLaunchDescriptionSource(os.path.join(get_package_share_directory(
            "vesc_ackermann"), 'launch', "ackermann_to_vesc_node.launch.xml")), launch_arguments=params.items(),
    ))

    components.append(launch.actions.IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory(
            "vesc_driver"), 'launch', "vesc_driver_node.launch.py")),
    ))

    return launch.LaunchDescription(components)
