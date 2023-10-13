import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny_edge_detector(image):    
    lane_image = np.copy(image)
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 50, 100)
    return canny

def region_of_interest(image):
    height, width = image.shape
    polygons = np.array([[(200, height), (1100, height), (550, 250)]])
    mask = np.zeros_like(image, np.uint8)
    cv2.fillPoly(mask, polygons, 255)
    return mask

image = cv2.imread('test_image.jpg')


canny = canny_edge_detector(image)
roi = region_of_interest(canny)
cv2.imshow("Result Image", roi)
cv2.waitKey(0)