from OpenGL.GL import *
import numpy as np

class Cuadrado:
   def __init__(self,l = 1,R = 1,G = 0,B = 0):
      
      self.vertices = np.matrix( [[-l/2,-l/2],
                                 [l/2, -l/2],
                                 [l/2,  l/2],
                                 [-l/2, l/2]],dtype = np.float32)

      self.R = R
      self.G = G
      self.B = B
   
   def getVertices(self):
      return self.vertices
   
   def trasladar(self, Tx, Ty):
      self.vertices += np.matrix([Tx, Ty],dtype = np.float32)
       
   def rotar(self, Θ):
      Θ = np.radians(Θ)
      
      self.vertices *= np.matrix([[np.cos(Θ),np.sin(Θ)],
                                  [- np.sin(Θ),np.cos(Θ)]],dtype = np.float32)  

   def escalar(self, Sx, Sy):
      self.vertices *= np.matrix([[Sx, 0],
                                  [0, Sy]],dtype = np.float32)
       
   def dibujar(self):
      glColor3f(self.R,self.G,self.B)   

      glBegin(GL_LINE_LOOP)
      for p in self.vertices:
         glVertex2fv(p)
         
      glEnd()
       
   def setColor(self,R,G,B):
      self.R = R
      self.G = G
      self.B = B


class Circunferencia:
   def __init__(self,r = 1,R = 1,G = 0,B = 0):

      self.vertices = [[r * np.cos(np.radians(Θ)),r * np.sin(np.radians(Θ))] for Θ in range(360)]

      self.R,self.G,self.B = R,G,B
    
   def getVertices(self):
      return self.vertices
   
   def trasladar(self,Tx,Ty):
      self.vertices+=np.matrix([Tx, Ty], dtype = np.float32)
       
   def rotar(self, Θ):
      Θ = np.radians(Θ)
      
      self.vertices *= np.matrix([[np.cos(Θ),  np.sin(Θ)],
                                  [- np.sin(Θ), np.cos(Θ)]], dtype = np.float32)
      
   def escalar(self,Sx,Sy):
      self.vertices *= np.matrix([[Sx, 0],[0, Sy]], dtype = np.float32)

   def dibujar(self):
      glColor3f(self.R,self.G,self.B)
      glBegin(GL_LINE_LOOP)

      for p in self.vertices:
         glVertex2fv(p)

      glEnd()
       
   def setColor(self,R,G,B):
      self.R = R
      self.G = G
      self.B = B
