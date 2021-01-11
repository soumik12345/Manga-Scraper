import img2pdf
from glob import glob


class PDFCreator:

    @staticmethod
    def create_pdf(image_dump_dir: str, pdf_location: str):
        image_dump_dir += '*'
        images = sorted(
            glob(image_dump_dir),
            key=lambda x: int(x.split('/')[-1].split('.')[0])
        )
        with open(pdf_location, 'wb') as f:
            f.write(img2pdf.convert(images))
