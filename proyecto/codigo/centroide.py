import numpy as np
import random
import math

class Centroide:
  def __init__(self,k,lista):
      self.var=math.inf ## varianza de la respuesta
      self.k=k ## cantidad de centroides
      self.lista=lista ## coordenadas de los puntos
      self.idx=[0]*len(lista) ## centroide de cada coordenada
      self.res=[0]*len(lista) ## respuesta, centroide de cada coordenada
      self.centroides=[0]*k ## coordenadas de los centroides
      self.centroides_pasados=[0]*k ## coordenadas de los centroides, iteracion pasada

  def update(self): ## calcula los nuevos centroides
    for i in range (0,self.k):
      self.centroides_pasados[i]=self.centroides[i]

    sum=[0]*self.k
    can=[0]*self.k
    for i in range (0,len(self.lista)):
      ind=self.idx[i]
      can[ind]=can[ind]+1
      sum[ind]=sum[ind]+self.lista[i]
    for i in range (0,self.k):
      if(can[i]==0): 
        continue
      self.centroides[i]=sum[i]//can[i]
    
  def check_varianza(self): ## revisa si la respuesta actual es mejor que las pasadas
    new_var=0
    for i in range (0,len(self.lista)):
      new_var=new_var+(self.lista[i]-self.centroides[self.idx[i]])*(self.lista[i]-self.centroides[self.idx[i]])
    if(new_var<self.var):
      self.var=new_var
      for i in range (0,len(self.lista)):
        self.res[i]=self.idx[i]


  def iter(self): ## actualiza el centroide de cada punto
    self.idx=[0]*len(self.lista)
    self.centroides=[]
    self.centroides_pasados=[0]*self.k
    for i in range (0,self.k):
      self.centroides.append(random.randint(0,255))
    self.centroides.sort()
    can=0
    while(self.centroides_pasados!=self.centroides):
      can=can+1
      for i in range (0,len(self.lista)):
        ind=0
        for j in range (0,self.k):
          if(abs(self.lista[i]-self.centroides[j])<abs(self.lista[i]-self.centroides[ind])):
            ind=j
        self.idx[i]=ind
      self.update()
    self.check_varianza()


  def respuesta(self):
    for i in range (0,len(self.lista)):
      self.idx[i]=self.res[i]
    self.update()

# este codigo fue creado por nosotros
  


