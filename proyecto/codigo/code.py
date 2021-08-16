import pandas as pd
import numpy as np
import os

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
  return 

main()