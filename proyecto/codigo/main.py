import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from centroide import Centroide as cn
import compresion as com

def load(path,plist):
  photos=[]
  for i in plist:
    newPath=path+"/"+i
    photo=pd.read_csv(newPath, header=None)
    mod_photo=np.array(photo).astype("int")
    photos.append(mod_photo)
  return photos


def main():
  path="C:/Users/ASUS/Documents/python/Proyecto datos/ST0245-Eafit-master/ST0245-Eafit-master/proyecto/datasets/csv/paraEntrenarYProbarLaIA/enfermo_test_csv"
  plist=os.listdir(path)
  photos=load(path,plist)
  print("fotos descargadas")
  img=photos[0] #ensayo de compresion para la primer foto
  com.comprimir(img)
  return 

main()