import cv2 
from collections import Counter 
 
img = cv2.imread('input_image.jpg', 0) 
freq = Counter(img.flatten()) 
print("Pixel Frequencies:", freq) 
