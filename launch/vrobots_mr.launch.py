from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    package_dir = FindPackageShare('ubi_vrobots_ros').find('ubi_vrobots_ros')

    # Path to your Python script relative to the package root
    python_script_path = os.path.join(package_dir, 'vr_bridge.py')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['python3', python_script_path],
            shell=True
        ),
        Node(
            package='ubi_vrobots_ros', 
            executable='mr', 
            name='multirotor_pubsub',  
            output='screen',             
        ),
    ])