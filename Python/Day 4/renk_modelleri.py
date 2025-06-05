import cv2
import numpy as np

image = cv2.imread("logo.png")

if image is None:
    print("Hata: Görüntü dosyası bulunamadı!")
    exit()

blue_channel, green_channel, red_channel = cv2.split(image)

cv2.imshow("Mavi Kanal",blue_channel)
cv2.imshow("Yesil Kanal",green_channel)
cv2.imshow("Kirmizi Kanal",red_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()

modified_image = cv2.merge([green_channel,red_channel,blue_channel])

cv2.imshow("Degistirilmis Renkler", modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("HSV", hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])

mask = cv2.inRange(hsv_image, lower_red, upper_red)

cv2.imshow("Maske", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()