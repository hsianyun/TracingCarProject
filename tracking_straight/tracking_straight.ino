/* IR road test v2.0 */

#include"config.h"
#include<SPI.h>

void MotorWriting(int, int);
int IR[5] = {38, 39, 40, 41, 42};
int IR_val[5] = {0,0,0,0,0};
float error = 0;
int error_count = 0;
int vL = 0, vR = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // Serial.println("Serial Port Connected!");
  for(int i=0; i<5; i++){
    pinMode(IR[i], INPUT);
  }
  pinMode(PWMR, OUTPUT);
  pinMode(RIN1, OUTPUT);
  pinMode(RIN1, OUTPUT);
  pinMode(LIN1, OUTPUT);
  pinMode(LIN2, OUTPUT);
  pinMode(PWML, OUTPUT);
}

void loop() {
  error = 0;
  error_count = 0;
  for(int i=0; i<5; i++){
    IR_val[i] = digitalRead(IR[i]);
    error_count += IR_val[i];
    // Serial.print("IR No."); 
    // Serial.print(i);
    // Serial.print(" Status: ");
    // Serial.println(IR_val[i]);
  }

  if(error_count >= 1){
    error = -1*IR_val[0]-0.5*IR_val[1] + 0.5*IR_val[3] + 1*IR_val[4]; //If IR sensor detect black, it returns 1. Else, it returns 0.
    error = error * 50;
  }
  vL = 200 + error ;
  vR = 200 - error ;
  
  if(vL>250){
    vL = 250;
  }
  if(vR>250){
    vR = 250;
  }
  // Serial.print("L: ");
  // Serial.println(vL);
  // Serial.print("R: ");
  // Serial.println(vR);  
  
  
  MotorWriting(vL, vR);
  delay(20);
}

void MotorWriting(int vL, int vR){
  int out_vL, out_vR;
  if(vL<0){
    out_vL = -vL;
    digitalWrite(LIN1, LOW);
    digitalWrite(LIN2, HIGH);
  }else{
    out_vL = vL;
    digitalWrite(LIN1, HIGH);
    digitalWrite(LIN2, LOW);
  }

  if(vR<0){
    out_vR = -vR;
    digitalWrite(RIN1, LOW);
    digitalWrite(RIN2, HIGH);
  }else{
    out_vR = vR;
    digitalWrite(RIN1, HIGH);
    digitalWrite(RIN2, LOW);
  }
  // Serial.print("L: ");
  // Serial.println(out_vL);
  // Serial.print("R: ");
  // Serial.println(out_vR);  
  analogWrite(PWMR, out_vR);
  analogWrite(PWML, out_vL);
  //delay(20);
}
