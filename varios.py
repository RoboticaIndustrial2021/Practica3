from robodk.robolink import *  # RoboDK API
from robodk.robomath import *
from robodk.robodialogs import *

from time import*
RDK = Robolink()


# Program example:
item1 = RDK.Item('box')
item2 = RDK.Item('cil')
frame3 = RDK.Item('Frame 3')


if item1.Valid():
    print('Item selected: ' + item1.Name())
    print('Item posistion: ' + repr(item1.Pose()))
    print('Item selected: ' + item2.Name())
    print('Item posistion: ' + repr(item2.Pose()))


print('Items in the station:')
itemlist = RDK.ItemList()
for i in itemlist:
 print(i.Name())

item1.Copy()
item1_Copy = frame3.Paste()

item2.Copy()
item2_Copy = frame3.Paste()
sleep(2)
martillo = RDK.MergeItems(list_items = [item1_Copy,item2_Copy])
martillo.setVisible(False)
posmartillo = martillo.Pose()
martillo.setPose(posmartillo*transl(0,100,0))
martillo.setName("martillo1_copy")
martillo.setVisible(True)
sleep(2)
martillo.Recolor([1,0,0,1])
RDK.ShowMessage("solicitando a usuario... ",False)
pedido = mbox("ingrese valor de escala en x,y,z desde 1 en adelante",entry="1,1,1")
x,y,z = [int(x.replace(' ','')) for x in  pedido.split(',')]
martillo.Scale([x,y,z])
RDK.ShowMessage("fin de programa ")
