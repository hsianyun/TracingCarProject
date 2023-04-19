
from BTinterface import BTinterface
import BT
object = BTinterface()
object.start()
while(True):
    if (object.ser.SerialReadString()):
        print('read string', object.ser.SerialReadString())
    if(object.ser.SerialReadByte()):
        print('rfid', object.ser.SerialReadByte())