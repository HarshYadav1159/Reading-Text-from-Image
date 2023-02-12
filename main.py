import cv2
import pytesseract
import numpy as np


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

img = cv2.imread('7.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Gaussian_blurred_1 = np.hstack([
#   cv2.GaussianBlur(img,(3,3),0),
#   cv2.GaussianBlur(img,(5,5),0),
#   cv2.GaussianBlur(img,(9,9),0)])
# cv2.imshow(Gaussian_blurred_1)

# sharpen_img = cv2.filter2D(img, -1, filter)
#
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 3)
print(pytesseract.image_to_string(img))
# print(pytesseract.image_to_boxes(sharpen_img))
cv2.imshow('Result', img)
cv2.waitKey(0)

