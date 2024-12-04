import cv2
import numpy as np
#cargamos imagen
image1 = cv2.imread('imagen1.jpg')

cv2.imshow('Image', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#obtener dimensiones de la imagen
image2 = cv2.imread('imagen2.jpg')
hight, width = image2.shape[:2]

center = (width/2, hight/2)

#rotar la imagen
image3 = cv2.imread('imagen3.jpg')
angulo = 45
matrix = cv2.getRotationMatrix2D(center, angulo, 1.0)
rotated = cv2.warpAffine(image3, matrix, (width, hight))

cv2.imshow('Image3', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

tx, ty = 100, 50
M = np.float32([[1, 0, tx], [0, 1, ty]])

translated = cv2.warpAffine(image3, M, (width, hight))

cv2.imshow('Image3', translated)
cv2.waitKey(0)
cv2.destroyAllWindows()

#escalar la imagen
image4 = cv2.imread('imagen4.jpg')
scale_percent = 50
width = int(image4.shape[1] * scale_percent / 100)
height = int(image4.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(image4, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('Image4', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Definir las coordenadas de la región de interés
image1 = cv2.imread('imagen1.jpg')
x1, y1, x2, y2 = 100, 100, 400, 400

# Extraer la región de interés
roi = image1[y1:y2, x1:x2]

# Mostrar la región de interés
image2 = cv2.imread('imagen2.jpg')
cv2.imshow('Región de interés', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
# suavizar 
# Aplicar un filtro Gaussiano
blur = cv2.GaussianBlur(image2, (5, 5), 0)

cv2.imshow('Image2', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()