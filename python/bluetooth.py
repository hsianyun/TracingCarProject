
from BTinterface import BTinterface
import BT
object = BTinterface()
object.start()
while(True):
    # read_str = object.ser.SerialReadString()
    # if (read_str):
    #     print('read string', read_str)
    # else:
    #     print('no str')
    uid = object.get_UID()
    if(uid):
        print('rfid', uid[2:])