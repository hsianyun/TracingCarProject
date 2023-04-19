from BTinterface import BTinterface
import BT
object = BTinterface()
object.start()
while(True):
    if (object.ser.SerialReadString):
        print(object.ser.SerialReadString)