import pandas as pd
import numpy as np
import os
import Compressor_kmn as kmn
import LZ_77_ccompressor as lz_77


def load(path,plist):
  photos=[]
  for i in plist:
    newPath=path+"/"+i
    photo=pd.read_csv(newPath, header=None)
    mod_photo=np.array(photo).astype("int")
    photos.append(mod_photo)
    # break ## para ensayar solo una foto
  return photos


def main():
  path="C:/Users/ASUS/Documents/python/Proyecto datos/ST0245-Eafit-master/ST0245-Eafit-master/proyecto/datasets/csv/paraEntrenarYProbarLaIA/enfermo_test_csv"
  plist=os.listdir(path)
  photos=load(path,plist)
  print("fotos descargadas")
  img=photos[0] #ensayo de compresion para la primer foto
  
  kmn.comprimir(img) #ensayo con k-means
  
  lz=lz_77.LZ77Compressor() #ensayo con lz77
  path_prueba="C:/Users/ASUS/Documents/python/Proyecto datos/ST0245-Eafit-master/ST0245-Eafit-master/proyecto/datasets/imagenes/gris/enfermo_gris"
  plist=os.listdir(path_prueba)
  path_prueba=path_prueba+"/"+plist[0]
  output_path="C:/Users/ASUS/Documents/python/Proyecto datos/imagenes comprimidas/LZ-77/ensayo"
  lz.compress(path_prueba, output_path)
  
  #se imprime la imagen compresa de k-means, y se guarda la compresion de lz_77 en el output_path
  return 0



main()