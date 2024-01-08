"""
para usar este codigo, se debe agregar almenos dos objetos cualquiera a la estacion
y añadir al menos dos frames
además añadir el codigo python acutal y ejecutarlo"""
from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox
from time import sleep
import random
# Link to RoboDK
RDK = Robolink()
objetoss = RDK.ItemList(ITEM_TYPE_OBJECT)
bott=RDK.ItemUserPick("seleccione objeto a clonar",objetoss)
bott.Copy()
framess = RDK.ItemList(ITEM_TYPE_FRAME)
frame=RDK.ItemUserPick("seleccione referencia \n donde se va a  clonar",framess)

def botss():
    itemss = RDK.ItemList()
    botes = []
    for k in itemss:
        if k.Name().startswith("bot"):
            botes.append(k)
    return botes

objetos = botss()
for i in objetos:
    i.setVisible(False)
    i.Delete()
def box_calc(size_xyz, pallet_xyz):
    """Calculates a list of points to store parts in a pallet"""
    [size_x, size_y, size_z] = size_xyz
    [pallet_x, pallet_y, pallet_z] = pallet_xyz    
    xyz_list = []
    for h in range(int(pallet_z)):
        for j in range(int(pallet_y)):
            for i in range(int(pallet_x)):
                xyz_list = xyz_list + [[(i+0.5)*size_x, (j+0.5)*size_y, (h+0.5)*size_z]]
    return xyz_list

possis = mbox("Ingrese distancia entre un objeto y otro",entry=[100,100,130])
cantid = mbox("Ingrese cuando clone desea en X, Y y Z",entry=[5,3,2])
posinit = box_calc([int(possis[0]),int(possis[1]),int(possis[2])],
                   [int(cantid[0]),int(cantid[1]),int(cantid[2])])


for i in range(len(posinit)):
    newbot = frame.Paste()
    newbot.setName('bot'+str(i))
    newbot.setPose(transl(posinit[i]))


objetos = botss()
for i in objetos:
    i.setVisible(True)


def rr(inf , may):
    return random.uniform(inf,may)

for i in range(len(posinit)):
    RDK.Item("bot"+str(i)).Recolor([rr(0,1),rr(0,1),rr(0,1),1])

