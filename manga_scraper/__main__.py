#!/usr/bin/python3

import os
import img2pdf
import subprocess
from tqdm import tqdm
from glob import glob

from .utils import preprocess_images, install_mangadl, split_list


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
