import cv2
import numpy as np

image = cv2.imread("random_items.jpeg") # Insert the name of the file here

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 100, 100], dtype="uint8") #Determine the lower HSV value of the color green, and insert them as your array values [h, s, v]
upper_green = np.array([85, 255, 255], dtype="uint8") #Determine the upper HSV value of the color green, and insert them as your array values [h, s, v]
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# Range 1: Covers the left side of the chart (0 to 10)
lower_red1 = np.array([0, 50, 40], dtype="uint8")
upper_red1 = np.array([10, 255, 255], dtype="uint8")
mask_red_1 = cv2.inRange(hsv, lower_red1, upper_red1)

# Range 2: Covers the right side of the chart (170 to 180)
lower_red2 = np.array([170, 50, 40], dtype="uint8")
upper_red2 = np.array([180, 255, 255], dtype="uint8")
mask_red_2 = cv2.inRange(hsv, lower_red2, upper_red2)

# Combine both masks to get full red coverage
mask_red = cv2.bitwise_or(mask_red_1, mask_red_2)


mask = cv2.bitwise_or(mask_green, mask_red)
detected_green_red = cv2.bitwise_and(hsv, hsv, mask= mask)

edited_image = cv2.cvtColor(detected_green_red, cv2.COLOR_HSV2BGR)

cv2.imwrite("battery_detected.jpg", edited_image)

cv2.imshow("Original Image", image)

cv2.imshow("Battery Detected", edited_image)

cv2.waitKey(0) #press any key to close the window



# ADD YOUR DETECT BOXCUTTER CODE BELOW











