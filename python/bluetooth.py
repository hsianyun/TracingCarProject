
from BTinterface import BTinterface
import BT
object = BTinterface()
object.start()
for i in range(1000):
    if (object.ser.SerialReadString()):
        print(object.ser.SerialReadString())
    else:
        print(i)
print('over')