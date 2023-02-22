import os
import launch
from launch_ros.actions import DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import TextSubstitution

from pathlib import Path


def generate_launch_description():

    speed_to_erpm_gain = DeclareLaunchArgument(
        "speed_to_erpm_gain", default_value=TextSubstitution(text="4614.0")
    )
    speed_to_erpm_offset = DeclareLaunchArgument(
        "speed_to_erpm_offset", default_value=TextSubstitution(text="0.0")
    )
    steering_angle_to_servo_gain = DeclareLaunchArgument(
        "steering_angle_to_servo_gain", default_value=TextSubstitution(text="-1.2135")
    )
    steering_angle_to_servo_offset = DeclareLaunchArgument(
        "steering_angle_to_servo_offset", default_value=TextSubstitution(text="0.5304")
    )

    params = {"speed_to_erpm_gain": speed_to_erpm_gain, "speed_to_erpm_offset": speed_to_erpm_offset,
              "steering_angle_to_servo_gain": steering_angle_to_servo_gain, "steering_angle_to_servo_offset": steering_angle_to_servo_offset}

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
