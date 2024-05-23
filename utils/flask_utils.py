import hashlib
import json
import os
import string
import random
import cv2

from datetime import datetime
from typing import Any
from PIL import Image

from classes.sql_connect import SQLManager


def check_stream_availability(url):
    cap = cv2.VideoCapture(url)
    if cap.isOpened():
        cap.release()
        return True
    return False

def save_img_base64(image_data, path):
    formatted_date = datetime.now().date().strftime("%Y-%m-%d")

    save_dir = f"{path}/{formatted_date}/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    new_file_name = f"{(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))}_" \
                    f"{''.join(random.choice(string.ascii_lowercase) for i in range(5))}"

    output_path = save_dir + new_file_name + '.png'

    with open(output_path, 'wb') as file:
        file.write(image_data)

    return output_path

def save_img(name, img, path):
    formatted_date = datetime.now().date().strftime("%Y-%m-%d")

    save_dir = f"{path}/{formatted_date}/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    new_file_name = f"{(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))}_" \
                    f"{''.join(random.choice(string.ascii_lowercase) for i in range(5))}_{name}"

    output_path = save_dir + new_file_name
    Image.fromarray(img).save(output_path)

    return output_path

def wrap_ok_return_value(data: Any) -> str:
    return json.dumps({
        'code': 200,
        'msg': 'complete！',
        'data': data
    })

def wrap_error_return_value(message: str) -> str:
    return json.dumps({
        'code': 500,
        'msg': message,
        'data': None
    })

def wrap_unauthorized_return_value(message: str) -> str:
    return json.dumps({
        'code': 401,
        'msg': message,
        'data': None
    })