
from BTinterface import BTinterface
import BT
object = BTinterface()
object.start()
while(True):
    # if (object.ser.SerialReadString()):
    #     print('read string', object.ser.SerialReadString())
    uid = object.get_UID()
    if(uid):
        print('rfid', uid)