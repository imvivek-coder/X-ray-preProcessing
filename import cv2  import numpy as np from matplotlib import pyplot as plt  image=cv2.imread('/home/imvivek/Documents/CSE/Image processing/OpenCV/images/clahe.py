import cv2 
import numpy as np
from matplotlib import pyplot as plt

image=cv2.imread('')

 
# Reading the image from the present directory
# Resizing the image for compatibility
image = cv2.resize(image, (500, 600))
 
# The initial processing of the image
# image = cv2.medianBlur(image, 3)
image_bw = image
 
# The declaration of CLAHE
# clipLimit -> Threshold for contrast limiting
clahe = cv2.createCLAHE(clipLimit = 5)
final_img = clahe.apply(image_bw)

final_img1=cv2.equalizeHist(image) 
# Ordinary thresholding the same image
_,ordinary_img = cv2.threshold(image_bw, 155, 255, cv2.THRESH_BINARY)
h=cv2.calcHist([image],[0],None,[256],[0,256])
h1=cv2.calcHist([final_img],[0],None,[256],[0,256])  
h2=cv2.calcHist([final_img1],[0],None,[256],[0,256]) 
# show the plotting graph of an image

fig, ax = plt.subplots(2,3)
ax[0][0].plot(h)
ax[0][1].plot(h1)
ax[0][2].plot(h2)
ax[1][0].imshow(image,cmap='gray',vmin=0,vmax=255)
ax[1][1].imshow(final_img,cmap='gray',vmin=0,vmax=255)
ax[1][2].imshow(final_img1,cmap='gray',vmin=0,vmax=255)
plt.show()

#plt.plot(h1)
#plt.show()
# Showing all the three images
"""
cv2.imshow("original",image)
cv2.imshow("ordinary threshold", ordinary_img)
cv2.imshow("CLAHE image", final_img)
cv2.imshow("Histograme Eq",final_img1)
cv2.waitKey(0)
"""
