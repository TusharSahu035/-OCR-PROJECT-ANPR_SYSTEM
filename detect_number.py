import cv2
import pytesseract
import numpy as np
import imutils

# Set Tesseract OCR path (Only for Windows, update if needed)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detect_number_plate(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection
    edged = cv2.Canny(gray, 50, 200)
    contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    number_plate = None
    for c in contours:
        approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
        if len(approx) == 4:  # Plate is usually rectangular
            number_plate = approx
            break

    if number_plate is None:
        return None

    # Mask everything except the number plate
    mask = np.zeros(gray.shape, np.uint8)
    cv2.drawContours(mask, [number_plate], 0, 255, -1)
    result = cv2.bitwise_and(image, image, mask=mask)

    # Convert to grayscale and apply OCR
    plate_text = pytesseract.image_to_string(result, config='--psm 8')
    return plate_text.strip()
