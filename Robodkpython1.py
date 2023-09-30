from robodk.robolink import *  # RoboDK API
from robodk.robomath import *
RDK = Robolink()    #se crea la variable que contiene la instancia Robolink que contine los comando o funciones a usar

#si existe mas de un robot en la estacion se muestra la lista de robots disponibles
#y el usuario debe seleccionar con que robot desea trabajar
robot = RDK.ItemUserPick('',ITEM_TYPE_ROBOT)    
#si no selecciona robot se cierra el programa
if not robot.Valid():
    quit()

reference = robot.Parent()    #devuelve a que frame está referenciado el robot actualmente
print (reference)
robot.setPoseFrame(reference)    #le indicamos al robot a que referencia queremos que esté relacionado
pose_ref=robot.Pose()    #devuelve la matriz de transformacion 4x4 del robot con respecto a la referencia anteriormente dado
print (pose_ref)
posi = Pose_2_TxyzRxyz(pose_ref)    #convierte la matriz de transformacion a valores x,y,x,y sus respectivos angulos
print (posi)
home_joints =  robot.JointsHome()    #devuelvee los valores por defecto de las articulaciones
print (home_joints)
#robot.MoveJ(home_joints)
pose_ref=robot.Pose()    #en la variable pose_ref se guarda la posición actual del robot

limitneg,limitpos,pp = robot.JointLimits()    #devuelve los valores limites de cada articulacion
print (limitneg,  "\n" ,limitpos ,"\n" )
aprox = 100    #variable para aproximar a un punto
#Creación de targets de la manera X,Y,Z
a0 = transl(-370,50,-50+aprox)     
a1 = transl(-370,50,-150)
a2 = transl(-370,50,50)
a3 = transl(-370,-150,50)
a4 = transl(-370,-150,-50)
a5 = transl(-370,50,-50)
a6 = transl(-370,-150,-150)

A = [a0, a1, a2, a3, a4,a5,a6]    #arreglo que contiene todos los targets

for i in range(len(A)):    #recorrido de targets
    robot.MoveJ(A[i]*rotx(-pi))    #movimento Joint de targets con una rotación -pi en X
