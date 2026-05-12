import cv2
img=cv2.imread("img_4k_resolution.jpg")
cv2.imshow("cv2.started",img)
cv2.waitKey(0)
cv2.imwrite("Cutted_Img.png",img)