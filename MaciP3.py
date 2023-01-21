# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/robodk.html

# You can also use the new version of the API:
from robodk.robolink import *    # RoboDK API
from robodk.robomath import *    # Robot toolbox
RDK = Robolink()

#adquirimos el objeto robot hacia una variable
robot = RDK.Item('Kawasaki RS03N')
#adquirimos el objeto frame2 hacia una variable
ref1 = RDK.Item('Frame 2')
#adquirimos el objeto frame3 hacia una variable
ref2 = RDK.Item('Frame 3')
#adquirimos el objeto target hacia una variable
target = RDK.Item('Target 1')

#cambiamos de referencia al robot
robot.setPoseFrame(ref1)
#adquirimos la posicion del target hacia una variable
pose_ref=target.Pose()

#creamos la variable aproximacion
aprox = -50

#creamos targets desplazados con respecto al target base
a0 = pose_ref*transl(0,0,0+aprox)
a1 = pose_ref*transl(0,0,0)
a2 = pose_ref*transl(75,0,0)
a3 = pose_ref*transl(0,50,0)
a4 = pose_ref*transl(75,100,0)
a5 = pose_ref*transl(0,100,0)
a6 = pose_ref*transl(0,100,0+aprox)

#se crea un arreglo con las posiciones creadas anteriormente
A = [a0, a1, a2, a3, a4, a5, a6]

def movimiento():
    #recorremos el arreglo para que el robot se mueva a cada posicion
    for i in range(len(A)):
        #realizamos movimiento lineal MoveL o articular MoveJ
        robot.MoveJ(A[i])

#llamamos a la funcion para ejecutar el movimiento
movimiento()
#cambiamos de referencia al robot
robot.setPoseFrame(ref2)
#adquirimos la posicion del target hacia una variable
pose_ref=target.Pose()
#llamamos a la funcion para ejecutar el movimiento
movimiento()
