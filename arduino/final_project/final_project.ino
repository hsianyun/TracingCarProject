/***************************************************************************/
// File       [final_project.ino]
// Author     [Erik Kuo]
// Synopsis   [Code for managing main process]
// Functions  [setup, loop, Search_Mode, Hault_Mode, SetState]
// Modify     [2020/03/27 Erik Kuo]
/***************************************************************************/

#define DEBUG// debug flag

// for RFID
#include <SPI.h>
#include <MFRC522.h>
#include "bluetooth.h"
/*===========================define pin & create module object================================*/
// BlueTooth
// BT connect to Serial1 (Hardware Serial)
// Mega               HC05
// Pin  (Function)    Pin
// 18    TX       ->  RX
// 19    RX       <-  TX
// TB6612, 請按照自己車上的接線寫入腳位(左右不一定要跟註解寫的一樣)
#define MotorR_I1      2 //定義 A1 接腳（右）
#define MotorR_I2      3 //定義 A2 接腳（右）
#define MotorR_PWMR    44//定義 ENA (PWM調速) 接腳
#define MotorL_I3      5 //定義 B1 接腳（左）
#define MotorL_I4      6 //定義 B2 接腳（左）
#define MotorL_PWML    45//定義 ENB (PWM調速) 接腳
// 循線模組, 請按照自己車上的接線寫入腳位
#define IRpin_LL 38
#define IRpin_L  39
#define IRpin_M  40
#define IRpin_R  41
#define IRpin_RR 42
// RFID, 請按照自己車上的接線寫入腳位
#define RST_PIN      9        // 讀卡機的重置腳位
#define SS_PIN       53       // 晶片選擇腳位
MFRC522 mfrc522(SS_PIN, RST_PIN);  // 建立MFRC522物件
/*===========================define pin & create module object===========================*/
bool start = false;
/*============setup============*/
void setup()
{
   //bluetooth initialization
   Serial3.begin(9600);
   //Serial window
   Serial.begin(9600);
   //RFID initial
   SPI.begin();
   mfrc522.PCD_Init();
   //TB6612 pin
   pinMode(MotorR_I1,   OUTPUT);
   pinMode(MotorR_I2,   OUTPUT);
   pinMode(MotorL_I3,   OUTPUT);
   pinMode(MotorL_I4,   OUTPUT);
   pinMode(MotorL_PWML, OUTPUT);
   pinMode(MotorR_PWMR, OUTPUT);
   //tracking pin
   pinMode(IRpin_LL, INPUT); 
   pinMode(IRpin_L, INPUT);
   pinMode(IRpin_M, INPUT);
   pinMode(IRpin_R, INPUT);
   pinMode(IRpin_RR, INPUT);

  #ifdef DEBUG
  Serial.println("Waiting for bluetooth!");
  #endif

  BT_CMD bt_cmd;
  while(!start){
    bt_cmd = ask_BT();
    if(bt_cmd == 5)
      start = true;
  }
  #ifdef DEBUG
  Serial.println("Start!");
  #endif
}
/*============setup============*/

/*=====Import header files=====*/
#include "RFID.h"
#include "track.h"
#include "node.h"
/*=====Import header files=====*/

/*===========================initialize variables===========================*/
int l2=0,l1=0,m0=0,r1=0,r2=0; //紅外線模組的讀值(0->white,1->black)
int _Tp=90;                   //set your own value for motor power
bool state=false;             //set state to false to halt the car, set state to true to activate the car
BT_CMD _cmd = NOTHING;        //enum for bluetooth message, reference in bluetooth.h line 2
bool send = false;            //if arduino ask python server
/*===========================initialize variables===========================*/

/*===========================declare function prototypes===========================*/
void Search();    // search graph
void SetState();  // switch the state
/*===========================declare function prototypes===========================*/

/*===========================define function===========================*/
void loop()
{
  if(!state) {    //In the node and hasn't received bluetooth signal
    MotorWriting(0,0);  //stop and wait for command
    // ask_BT();
  }
  else Search();
  SetState();
}

void SetState()
{
  // TODO:
  int l2 = digitalRead(IRpin_LL), l1 = digitalRead(IRpin_L), m0 = digitalRead(IRpin_M);
  int r1 = digitalRead(IRpin_R), r2 = digitalRead(IRpin_RR);

  //十字循跡
  bool inCenter = false;
  state = true;
  tracking(l2, l1, m0, r1, r2);
  if (in_the_node(l2, l1, m0, r1, r2) && !inCenter)  {
    right_turn();
    inCenter = !inCenter;
  }

  //一般控制
  
  if (in_the_node(l2, l1, m0, r1, r2))  {
    /*
      when the car is in node, send 'n' to python and wait until received cmd
      then when it move out of the node, send 'o' to python
      */
    state = false;
    if(!send){
      send_msg('n');    //ask the server where to go
      send = true;
    }
    int direction = ask_BT(); //if we didn't received anything, direction == 0
    switch(direction) {
      case 0:
        state = false;  break;
      case 1:
        state = true; go_straight(); send = false; send_msg('o'); break;
      case 2:
        state = true; reverse_turn(); send = false; send_msg('o'); break;
      case 3:
        state = true; left_turn(); send = false; send_msg('o'); break;
      case 4:
        state = true; right_turn(); send = false; send_msg('o'); break;
      
    }
  }
  else  {
    tracking(l2, l1, m0, r1, r2);
    state = true;
  }
  // 1. Get command from bluetooth 
  // 2. Change state if need
}

void Search()
{
  byte *idSize = new byte[4];
  if (rfid(*idSize) != 0) {
    send_byte(rfid(*idSize), *idSize);
  }
  // TODO: let your car search graph(maze) according to bluetooth command from computer(python code)
}
/*===========================define function===========================*/
