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
            #cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 255), 2)
            cv2.line(lane_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    return lane_image
def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    pass

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        #print(parameters)
        slope, intercept = parameters[0], parameters[1]
        if slope <0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
        
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)

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
lines = cv2.HoughLinesP(roi, 2, np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5)

avergaed_lines = average_slope_intercept(lane_image, lines)

line_image = display_line(roi, lines, lane_image)

#combination = cv2.addWeighted(lane_image, 0.8, line_image, 1, 0)

cv2.imshow("Result Image", line_image)
cv2.waitKey(0)