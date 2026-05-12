import cv2
image=cv2.imread("img_4k_resolution.jpg")
shape=image.shape
print("shape",shape)
print("height of image",shape[0])
print("width of image",shape[1])
print("color channel of image",shape[2])
cv2.imshow("show",image)
cv2.waitKey(0)