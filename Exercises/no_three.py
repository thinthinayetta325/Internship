import cv2
image=cv2.imread("img_4k_resolution.jpg")
(b,g,r)=image[0,0]
print ("Blue =%d, Green = %d, Red=%d" %(b,g,r))
image[0,0]=(0,255,0)
(b,g,r)=image[0,0]
print("Blue =%d, Green = %d, Red=%d" %(b,g,r))
image[0:100,0:100]=(255,0,0)
cv2.imshow("Image",image)
cv2.waitKey(0)