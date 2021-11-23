#!/usr/bin/python3

import os
import cv2
import img2pdf
import subprocess
from tqdm import tqdm
from glob import glob
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


def download():

    manga_url = input("Enter Manga URL: ")
    
    pdf_location = "./dump"
    if not os.path.isdir(pdf_location):
        os.mkdir(pdf_location)
    
    download_comic = input("Do you want to download the comic? [y/n] ").lower() == "y"
    if download_comic:
        subprocess.run(["mangadl", manga_url, "-d", "./dump"])
    
    chapters = sorted(glob("dump/*/*"), key=lambda x: float(x.split('/')[-1].split('.')[0]))
    comic_name = chapters[0].split("/")[-2]
    
    compile_into_single = input("Do you want to compile all chapters to single pdf file? [y/n] ").lower() == "y"
    
    if not compile_into_single:

        pdf_dir = os.path.join(pdf_location, "pdf_files")
        if not os.path.isdir(pdf_dir):
            os.mkdir(pdf_dir)

        print("Creating PDFs...")
        for chapter in tqdm(chapters):
            image_files = sorted(
                glob(os.path.join(chapter, "*.jpg")),
                key=lambda x: float(x.split('/')[-1].split('.')[0])
            )
            preprocess_images(image_files)
            pdf_path = os.path.join(pdf_dir, chapter.split('/')[-1] + ".pdf")
            with open(pdf_path, 'wb') as f:
                f.write(img2pdf.convert(image_files))
        
        print(f"You pdfs are ready at {pdf_dir}")
    
    else:
        all_image_files = []
        for chapter in chapters:
            image_files = sorted(
                glob(os.path.join(chapter, "*.jpg")),
                key=lambda x: int(x.split('/')[-1].split('.')[0])
            )
            all_image_files += image_files
        print("Preprocessing all images...")
        preprocess_images(all_image_files, apply_prog_bar=True)
        print("Compiling PDF...")
        pdf_path = os.path.join(pdf_location, f"{comic_name}.pdf")
        with open(pdf_path, 'wb') as f:
            f.write(img2pdf.convert(all_image_files))
        print(f"You pdf is ready at {pdf_path}")
    
    os.system("rm -rf \"./dump/" + comic_name + "\"")


if __name__ == '__main__':
    download()
