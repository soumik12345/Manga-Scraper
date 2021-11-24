import cv2
import numpy as np
from typing import List, Tuple


def extract_panel_coordinates(image_file: str) -> List[Tuple]:
    image = cv2.imread(image_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh_inv = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    blur = cv2.GaussianBlur(thresh_inv, (1, 1), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    mask = np.ones(image.shape[:2], dtype="uint8") * 255
    boxes = []
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w * h > 1000:
            cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 0, 255), -1)
            boxes.append((x, y, w, h))
    # result = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
    return boxes
