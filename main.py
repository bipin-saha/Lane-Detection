import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny_edge_detector(image):    
    #lane_image = np.copy(image)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 50, 100)
    return canny

def display_line(image, lines, lane_image):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 255), 2)
            cv2.line(lane_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    return lane_image

def region_of_interest(image):
    height, width = image.shape
    polygons = np.array([[(200, height), (1100, height), (550, 250)]])
    mask = np.zeros_like(image, np.uint8)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)

canny = canny_edge_detector(image)
roi = region_of_interest(canny)
lines = cv2.HoughLinesP(roi, 2, np.pi/180, 100, np.array([]), minLineLength = 100, maxLineGap = 5)
line_image = display_line(roi, lines, lane_image)

#combination = cv2.addWeighted(lane_image, 0.8, line_image, 1, 0)

cv2.imshow("Result Image", line_image)
cv2.waitKey(0)