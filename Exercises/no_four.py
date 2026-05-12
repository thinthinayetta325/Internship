import cv2
img=cv2.imread("img_4k_resolution.jpg")
cx,cy=img.shape[1]//2,img.shape[0]//2 # Use integer division (//)
Endx,Endy=img.shape[1],img.shape[0]

TL=img[0:cy,0:cx]
TR=img[0:cy,cx:Endx]
BL=img[cy:Endy,0:cx]
BR=img[cy:Endy,cx:Endx]

cv2.imshow("Top Left",TL)
cv2.imshow("Top Right",TR)
cv2.imshow("Bottom Left",BL)
cv2.imshow("Bottom Right",BR)

cv2.waitKey(0)