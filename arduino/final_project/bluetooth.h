/***************************************************************************/
// File			  [bluetooth.h]
// Author		  [Erik Kuo]
// Synopsis		[Code for bluetooth communication]
// Functions  [ask_BT, send_msg, send_byte]
// Modify		  [2020/03/27 Erik Kuo]
/***************************************************************************/

/*if you have no idea how to start*/
/*check out what you have learned from week 2*/

enum BT_CMD {
  NOTHING, FORWARD, BACKWORD, LEFT, RIGHT
  // TODO: add your own command type here
};

BT_CMD ask_BT(){
    BT_CMD message=NOTHING;
    char cmd;
    if(Serial3.available()){
      if (Serial3.read() == 'w')
        message = FORWARD;
      else if (Serial3.read() == 'a')
        message = LEFT;
      else if (Serial3.read() == 's')
        message = BACKWORD;
      else if (Serial3.read() == 'd')
        message = RIGHT;
      cmd = Serial3.read();
      #ifdef DEBUG
      Serial.print("cmd : ");
      Serial.println(cmd);
      #endif
    }
    return message;
}// ask_BT

// send msg back through Serial3(bluetooth serial)
// can use send_byte alternatively to send msg back
// (but need to convert to byte type)
void send_msg(const char& msg)
{
//  size_t len = strlen(msg);
//  for (size_t i = 0 ; i < len; i++)  {
//    Serial3.write(msg[i]);
//  }
  Serial3.println(msg);
}// send_msg

// send UID back through Serial3(bluetooth serial)
void send_byte(byte *id, byte& idSize) {
  for (byte i = 0; i < idSize; i++) {  // Send UID consequently.
    Serial3.write(id[i]);
  }
  #ifdef DEBUG
  Serial.print("Sent id: ");
  for (byte i = 0; i < idSize; i++) {  // Show UID consequently.
    Serial.print(id[i], HEX);
  }
  Serial.println();
  #endif
}// send_byte
