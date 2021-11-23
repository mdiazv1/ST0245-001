
import matplotlib.pyplot as plt
from centroide import Centroide as cn
"""
comprimir llama los metodos de centroide.py para comprimir una matriz de la imagen
"""
def comprimir(img):


  iter=1
  img_x=len(img[0])
  print(img_x)
  img_y=len(img)
  print(img_y)
  desc=[[0 for y in range(img_x)] for x in range(img_y)] 
  comp=[[0 for y in range(img_x)] for x in range(img_y)] 
  lista=[]

  for i in range (0,img_y):
    for j in range (0,img_x):
      lista.append(img[i][j])

  img1=cn(16,lista)

  #comprime la imagen
  for i in range(iter):
    img1.iter()
  img1.respuesta()

  for i in range (0,len(img1.lista)):
    img1.lista[i]=img1.res[i]

  for i in range (0,img_y):
    for j in range (0,img_x):
      desc[i][j]=img1.centroides[img1.lista[i*img_x+j]]
      comp[i][j]=img1.lista[0] 


  print("compresion lista")

  img1plot = plt.imshow(desc)
  plt.show()
  print(comp)
  print(img1.centroides)
  return (comp, img1.centroides)