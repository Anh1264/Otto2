# utils.py
import requests

def notify_mcu(robot_id, status):
    """
    Notify the MCU of the robot's status change.
    
    Args:
        robot_id (int): The ID of the robot.
        status (bool): The new status of the robot (True for on, False for off).
    """
    # mcu_url = 'http://mcu_endpoint/api/robot_status_update'  # Replace with your MCU's endpoint

    # payload = {
    #     'robot_id': robot_id,
    #     'status': status
    # }

    # try:
    #     response = requests.post(mcu_url, json=payload)
    #     response.raise_for_status()  # Raise an exception for HTTP errors
    # except requests.exceptions.RequestException as e:
    #     print(f"Failed to notify MCU: {e}")
    print("Robot ID:", robot_id, "Robot Status:", status)