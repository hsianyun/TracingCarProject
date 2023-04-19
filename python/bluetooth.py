from BTinterface import BTinterface
import BT
object = BTinterface()
object.start()
print(object.ser.SerialReadString)
