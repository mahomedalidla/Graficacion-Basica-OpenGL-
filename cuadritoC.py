from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import numpy as np
#from CopiaGraC20 import *#Nombre de archivo .py
from CopiaGraC20 import ObjetoGrafico2D

def display(): 

    print("display")
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POINTS)
    glColor3f(0, 0, 0)

    for i in range(-250,251):
        glVertex2i(i,0)
        glVertex2i(0,i)

    glEnd()

  

    glFlush()

def special(key, x, y):
    
    MT.transfromar(MT)

    glutPostRedisplay()
    
def reshape(winW, winH):

    print("reshape", winW, winH)
    glViewport(0, 0, winW, winH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-winW/2, winW/2,-winH/2, winH/2)

########################
vertices = np.array([[x,x*np.sin(x)]
                    for x in np.linespace(-15,15,200)],dtype=np.float32)
obj1 = CopiaGraC20.ObjetoGrafico2D(vertices)
#
MT= np.array([[0.9,0,0],
              [0,0.9,0],
              [0,0,1]],dtype=np.float32)

#inicio    
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(100,100)
glutInitWindowSize(500,500)
glutCreateWindow(b'Nombre Ventana')
glClearColor(1,1,1,0) #red, green, blue, alpha
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutSpecialFunc(special)
glutMainLoop()





