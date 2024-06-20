from datetime import datetime, timedelta
import math
import base64
from .google_drive import upload_file_to_drive
def parts_file_name(file_name):
    file_name = file_name[0:file_name.index('.')]
    file_name_parts = file_name.split('x')
    return file_name_parts

def get_status(file_name_parts):
    status = file_name_parts[3]
    if status == 'ON':
        return True
    return False

def get_cap_time(file_name_parts):
    time_part = file_name_parts[2]
    date_format = "%Y-%m-%d_%H-%M-%S"
    cap_time = datetime.strptime(time_part, date_format)
    return cap_time

def get_inf_data(file_name_parts):
    inference_part = int(file_name_parts[0])
    inference = inference_part - 230000
    inf_result = math.floor(inference/1000)
    inf_conf = inference % 1000
    return inf_result, inf_conf

def get_inference_ms(file_name_parts):
    ms = int(file_name_parts[1])
    inference_ms = timedelta(milliseconds=ms)
    return inference_ms

def get_drive_link(file_data, file_name, folder_name):
    link = upload_file_to_drive(file_data, file_name, folder_name)
    print('link:', link)
    return link

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        base64_string = base64.b64encode(img_file.read()).decode('utf-8')
    return base64_string

def save_base64_image(base64_string, file_path):
    # Decode base64 string to binary image data
    binary_data = base64.b64decode(base64_string)

    # Write binary data to a file
    with open(file_path, 'wb') as file:
        file.write(binary_data)

    print(f"Image saved at: {file_path}")
