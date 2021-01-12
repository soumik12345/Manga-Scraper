import os
# import img2pdf
from glob import glob
from PIL import Image
from tqdm import tqdm


# class PDFCreator:

#     @staticmethod
#     def create_pdf(image_dump_dir: str, pdf_location: str):
#         images = [str(os.path.join(image_dump_dir, image)) for image in os.listdir(image_dump_dir)]
#         images = sorted(
#             images,
#             key=lambda x: int(x.split('/')[-1].split('.')[0])
#         )
#         with open(pdf_location, 'wb') as f:
#             f.write(img2pdf.convert(images))


class PDFCreator:

    @staticmethod
    def create_pdf(image_dump_dir: str, pdf_location: str):
        images = [str(os.path.join(image_dump_dir, image)) for image in os.listdir(image_dump_dir)]
        images = sorted(
            images,
            key=lambda x: int(x.split('/')[-1].split('.')[0])
        )
        images = [Image.open(image) for image in tqdm(images)]
        images[0].save(
            pdf_location, "PDF" , resolution = 100.0,
            save_all = True, append_images = images
        )
