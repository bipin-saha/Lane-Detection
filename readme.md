# Lane Detection Using OpenCV

## High-Level Overview
1. **Image Preprocessing:**
   - Convert the image to grayscale using the `cv2.cvtColor` function with `cv2.COLOR_RGB2GRAY`. This step reduces computational complexity.
   - Apply Gaussian blur to the grayscale image using `cv2.GaussianBlur` with a kernel size of (5, 5) to smoothen the image, filter noise, and capture edges effectively.

2. **Edge Detection:**
   - Utilize the Canny edge detection algorithm with the `cv2.Canny` function. This algorithm computes gradients and detects rapid changes in pixel intensity across all directions by applying derivative changes in pixels.

3. **Region of Interest (ROI) Selection:**
   - Define a region of interest using a polygon with the `cv2.fillPoly` function. This polygon focuses only on the relevant area for lane detection, typically the road area.
   - Perform a bitwise AND operation with the `cv2.bitwise_and` function to isolate the region of interest.

4. **Line Detection:**
   - Utilize the Hough Transformation for line detection using the `cv2.HoughLinesP` function. This method detects straight lines within the region of interest.

5. **Averaging Lane Lines:**
   - Compute the slopes and intercepts of detected lines separately for the left and right lanes using the `np.polyfit` function.
   - Average the slopes and intercepts for each lane using the `np.average` function to obtain a single averaged slope and intercept for each lane.

6. **Displaying the Output:**
   - Display the detected lane lines on the original image using the `cv2.line` function to draw lines on the lane image.

The provided code implements a lane detection system using OpenCV in Python. It follows these steps to detect lanes in images or video feeds, providing a visual representation of the detected lane lines over the original image or video.
