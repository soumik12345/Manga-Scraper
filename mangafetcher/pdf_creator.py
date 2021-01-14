import os
import img2pdf
from glob import glob
from PIL import Image
from .utils import preprocess_images


class PDFCreator:

    @staticmethod
    def create_pdf(image_dump_dir: str, pdf_location: str):
        image_dump_dir += '*'
        images = sorted(
            glob(image_dump_dir),
            key=lambda x: int(x.split('/')[-1].split('.')[0])
        )
        preprocess_images(images)
        with open(pdf_location, 'wb') as f:
            f.write(img2pdf.convert(images))


class PDFCreatorAlternate:

    @staticmethod
    def create_pdf(image_dump_dir: str, pdf_location: str):
        images = [
            str(os.path.join(image_dump_dir, image))
            for image in os.listdir(image_dump_dir)
        ]
        images = sorted(
            images,
            key=lambda x: int(x.split('/')[-1].split('.')[0])
        )
        preprocess_images(images)
        images = [Image.open(image) for image in images]
        images[0].save(
            pdf_location, "PDF", resolution=100.0,
            save_all=True, append_images=images
        )
