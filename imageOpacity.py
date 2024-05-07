import cv2 as cv

# Load the image  and increase the opacity
img = cv.imread("./images/flower.jpg")
alpha = 2.0
beta = 50
new_image = cv.addWeighted(img, alpha, img, 0, beta)

# Display the image
cv.imshow("Original Image", img)
cv.imshow("New Image", new_image)
cv.waitKey(0)
cv.destroyAllWindows()







