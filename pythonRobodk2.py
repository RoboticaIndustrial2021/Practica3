from robodk.robolink import *  # RoboDK API
from robodk.robomath import *
RDK = Robolink()

robot = RDK.ItemUserPick('',ITEM_TYPE_ROBOT)
if not robot.Valid():
    quit()
pose_ref=robot.Pose()    #en la variable pose_ref se guarda la posición actual del robot


aprox = -50
a0 = pose_ref*transl(0,0,0+aprox)    #Crear target a partir de un target fijo, con el desplazamiento en X,Y,Z
a1 = pose_ref*transl(0,0,0)
a2 = pose_ref*transl(75,0,0)
a3 = pose_ref*transl(0,50,0)
a4 = pose_ref*transl(75,100,0)
a5 = pose_ref*transl(0,100,0)
a6 = pose_ref*transl(0,100,0+aprox)

A = [a0, a1, a2, a3, a4, a5, a6]
for i in range(len(A)):
    robot.MoveJ(A[i])
