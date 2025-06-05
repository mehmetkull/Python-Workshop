import cv2

image = cv2.imread("logo.png")

if image is None:
    print("Hata: Görüntü dosyası bulunamadı!")
    exit()

new_width = 400
new_height = int(image.shape[0] * (new_width / image.shape[1]))

resized_image = cv2.resize(image, (new_width, new_height))

cv2.imwrite("resize_logo.png",resized_image)

h, w, c = resized_image.shape

print(f"Görüntü Boyutları: {w}x{h} piksel, {c} kanal")

rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("rotated_90.png",rotated_90)

cropped_image = image[50:250, 50:250]

cv2.imshow("rotated_90.png",cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()