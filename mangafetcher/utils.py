import os
import cv2
import shutil
import requests
from tqdm import tqdm
from typing import List
from requests_html import HTMLSession


def get_content(url: str, allow_redirects: bool = True) -> str:
    response = requests.get(url, allow_redirects=allow_redirects)
    content = response.content.decode()
    return content


def get_rendered_content(url: str) -> str:
    session = HTMLSession()
    response = session.get(url)
    return response


def make_directory(dir_name: str):
    try:
        os.mkdir(dir_name)
    except Exception as e:
        pass


def remove_directory(dir_name: str):
    try:
        shutil.rmtree('./dump/')
    except Exception as e:
        pass


def preprocess_images(file_paths: List[str]):
    print("Preprocessing Images....")
    for image_file in tqdm(file_paths):
        image = cv2.imread(image_file)
        os.remove(image_file)
        cv2.imwrite(image_file, image)
