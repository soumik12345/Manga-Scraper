import os
import cv2
import subprocess
from tqdm import tqdm
from typing import List


def preprocess_images(file_paths: List[str], apply_prog_bar: bool = False):
    iterable = file_paths if not apply_prog_bar else tqdm(file_paths)
    for image_file in iterable:
        image = cv2.imread(image_file)
        os.remove(image_file)
        cv2.imwrite(image_file, image)


def split_list(given_list: List, chunk_size: int) -> List:
    return [
        given_list[offs : offs + chunk_size]
        for offs in range(0, len(given_list), chunk_size)
    ]


def install_mangadl():
    try:
        subprocess.check_output(["mangadl"])
    except:
        print("installing mangadl")
        os.system(
            "curl --compressed -s https://raw.githubusercontent.com/Akianonymus/mangadl-bash/master/release/install | bash -s"
        )
        print("mangadl installed")
