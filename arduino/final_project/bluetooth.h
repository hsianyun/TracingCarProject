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
    if(Serial1.available()){
      if (char(Serial.read() == 'w'))
        message = FORWARD;
      else if (char(Serial.read() == 'a'))
        message = LEFT;
      else if (char(Serial.read() == 's'))
        message = BACKWORD;
      else if (char(Serial.read() == 'd'))
        message = RIGHT;
      cmd = Serial.read();
      #ifdef DEBUG
      Serial.print("cmd : ");
      Serial.println(cmd);
      #endif
    }
    return message;
}// ask_BT

// send msg back through Serial1(bluetooth serial)
// can use send_byte alternatively to send msg back
// (but need to convert to byte type)
void send_msg(const char& msg)
{
  int ScharLength = Serial.available();
  if(Serial.available()){
    for(int j=0; j<ScharLength; j++){
      Serial1.write(Serial.read());
    }
  }
}// send_msg

// send UID back through Serial1(bluetooth serial)
void send_byte(byte *id, byte& idSize) {
  for (byte i = 0; i < idSize; i++) {  // Send UID consequently.
    Serial1.write(id[i]);
  }
  #ifdef DEBUG
  Serial.print("Sent id: ");
  for (byte i = 0; i < idSize; i++) {  // Show UID consequently.
    Serial.print(id[i], HEX);
  }
  Serial.println();
  #endif
}// send_byte
