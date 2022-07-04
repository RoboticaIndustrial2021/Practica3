from robodk.robolink import *  # RoboDK API
from robodk.robomath import *
RDK = Robolink()

robot = RDK.ItemUserPick('',ITEM_TYPE_ROBOT)
if not robot.Valid():
    quit()
reference = robot.Parent()
print (reference)
robot.setPoseFrame(reference)
pose_ref=robot.Pose()
print (pose_ref)
posi = Pose_2_TxyzRxyz(pose_ref)
print (posi)
home_joints =  robot.JointsHome()
print (home_joints)
#robot.MoveJ(home_joints)
pose_ref=robot.Pose()

limitneg,limitpos,pp = robot.JointLimits()
print (limitneg,  "\n" ,limitpos ,"\n" )
aprox = 100
a0 = transl(-370,50,-50+aprox) 
a1 = transl(-370,50,-150)
a2 = transl(-370,50,50)
a3 = transl(-370,-150,50)
a4 = transl(-370,-150,-50)
a5 = transl(-370,50,-50)
a6 = transl(-370,-150,-150)

A = [a0, a1, a2, a3, a4,a5,a6]

for i in range(len(A)):
    robot.MoveJ(A[i]*rotx(-pi))
