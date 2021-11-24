import os
import cv2
import img2pdf
import subprocess
import numpy as np
from tqdm import tqdm
from glob import glob
from typing import List, Tuple


def extract_panel_coordinates(
    image: np.ndarray, panel_area_threshold: int = 1000
) -> List[Tuple]:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh_inv = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    blur = cv2.GaussianBlur(thresh_inv, (1, 1), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    mask = np.ones(image.shape[:2], dtype="uint8") * 255
    boxes = []
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w * h > panel_area_threshold:
            cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 0, 255), -1)
            boxes.append((x, y, w, h))
    return boxes


def preprocess_images(
    file_paths: List[str],
    apply_prog_bar: bool = False,
    apply_panel_extraction: bool = False,
):
    iterable = file_paths if not apply_prog_bar else tqdm(file_paths)
    if apply_panel_extraction:
        counter = 1
        for image_file in iterable:
            image_path = "/".join([i for i in file_paths[0].split("/")[:-1]])
            panel_dir = os.path.join(image_path, "panels")
            if not os.path.isdir(panel_dir):
                os.mkdir(panel_dir)
            image = cv2.imread(image_file)
            boxes = extract_panel_coordinates(image, panel_area_threshold=10000)
            for box in boxes:
                x, y, w, h = box
                panel = image[y : y + h, x : x + w]
                cv2.imwrite(os.path.join(panel_dir, str(counter) + ".jpg"), panel)
                counter += 1
    else:
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

    pdf_location = "./dump"
    if not os.path.isdir(pdf_location):
        os.mkdir(pdf_location)

    download_comic = input("Do you want to download the comic? [y/n] ").lower() == "y"
    if download_comic:
        manga_url = input("Enter Manga URL: ")
        subprocess.run(["mangadl", manga_url, "-d", "./dump"])

    chapters = sorted(
        glob("dump/*/*"), key=lambda x: float(x.split("/")[-1].split(".")[0])
    )
    comic_name = chapters[0].split("/")[-2]

    compile_into_single = (
        input("Do you want to compile all chapters to single pdf file? [y/n] ").lower()
        == "y"
    )

    apply_panel_extraction = (
        input(
            "Do you want to apply experimental panel extraction on all pages? [y/n] "
        ).lower()
        == "y"
    )

    if not compile_into_single:

        pdf_dir = os.path.join(pdf_location, "pdf_files")
        if not os.path.isdir(pdf_dir):
            os.mkdir(pdf_dir)

        print("Creating PDFs...")
        print(chapters)
        for chapter in tqdm(chapters):
            image_files = sorted(
                glob(os.path.join(chapter, "*.jpg")),
                key=lambda x: float(x.split("/")[-1].split(".")[0]),
            )
            preprocess_images(
                image_files, apply_panel_extraction=apply_panel_extraction
            )
            if apply_panel_extraction:
                image_files = sorted(
                    glob(os.path.join(chapter, "panels", "*.jpg")),
                    key=lambda x: float(x.split("/")[-1].split(".")[0]),
                )
            pdf_path = os.path.join(pdf_dir, chapter.split("/")[-1] + ".pdf")
            with open(pdf_path, "wb") as f:
                f.write(img2pdf.convert(image_files))

        print(f"You pdfs are ready at {pdf_dir}")

    else:
        all_image_files = []
        for chapter in chapters:
            image_files = sorted(
                glob(os.path.join(chapter, "*.jpg")),
                key=lambda x: int(x.split("/")[-1].split(".")[0]),
            )
            all_image_files += image_files
        print("Preprocessing all images...")
        preprocess_images(
            all_image_files,
            apply_prog_bar=True,
            apply_panel_extraction=apply_panel_extraction,
        )
        print("Compiling PDF...")
        pdf_path = (
            os.path.join(pdf_location, f"{comic_name}.pdf")
            if not apply_panel_extraction
            else os.path.join(pdf_location, f"{comic_name} (panelled).pdf")
        )
        if apply_panel_extraction:
            all_image_files = []
            for chapter in chapters:
                image_files = sorted(
                    glob(os.path.join(chapter, "panels", "*.jpg")),
                    key=lambda x: int(x.split("/")[-1].split(".")[0]),
                )
                all_image_files += image_files
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(all_image_files))
        print(f"You pdf is ready at {pdf_path}")

    # os.system("rm -rf \"./dump/" + comic_name + "\"")


if __name__ == "__main__":
    download()
