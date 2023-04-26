/***************************************************************************/
// File			  [track.h]
// Author		  [Erik Kuo]
// Synopsis		[Code used for tracking]
// Functions  [MotorWriting, MotorInverter, tracking]
// Modify		  [2020/03/27 Erik Kuo]
/***************************************************************************/

/*if you have no idea how to start*/
/*check out what you have learned from week 1 & 6*/
/*feel free to add your own function for convenience*/

/*===========================import variable===========================*/
int extern _Tp;
/*===========================import variable===========================*/

// Write the voltage to motor.
void MotorWriting(double vL, double vR) {
  // TODO: use TB6612 to control motor voltage & direction
  int out_vL, out_vR;
  if(vL<0){
    out_vL = -vL;
    digitalWrite(MotorL_I3, LOW);
    digitalWrite(MotorL_I4, HIGH);
  }else{
    out_vL = vL;
    digitalWrite(MotorL_I3, HIGH);
    digitalWrite(MotorL_I4, LOW);
  }

  if(vR<0){
    out_vR = -vR;
    digitalWrite(MotorR_I1, LOW);
    digitalWrite(MotorR_I2, HIGH);
  }else{
    out_vR = vR;
    digitalWrite(MotorR_I1, HIGH);
    digitalWrite(MotorR_I2, LOW);
  }
  analogWrite(MotorR_PWMR, out_vR);
  analogWrite(MotorL_PWML, out_vL);
  delay(5);
}// MotorWriting

// Handle negative motor_PWMR value. 
void MotorInverter(int motor, bool& dir) {
  //Hint: the value of motor_PWMR must between 0~255, cannot write negative value.
}// MotorInverter

// P/PID control Tracking
void tracking(int l2, int l1, int m0, int r1, int r2){
  // find your own parameters!
  double _w0 = 0;
  double _w1 = 0.5;
  double _w2 = 1;
  double _Kp = l2+l1+m0+r1+r2;
  double _Kd; // d term parameter (optional) 
  double _Ki; // i term parameter (optional) (Hint: 不要調太大)
  double error=l2*_w2+l1*_w1+m0*_w0+r1*(-_w1)+r2*(-_w2);
  double vR = 200, vL = 200; // 馬達左右轉速原始值(從PID control 計算出來)。Between -255 to 255.
  double adj_R=1, adj_L=1;   // 馬達轉速修正係數。MotorWriting(_Tp,_Tp)如果歪掉就要用參數修正。
    
  // TODO: complete your P/PID tracking code
  if(_Kp>0){
    error *= 50;
    vR += error;
    vL -= error;
  }else{
    vL = 200;
    vR = 0;
  }
  if(vL>250){
    vL = 250;
  }
  if(vR>250){
    vR = 250;
  }
  // end TODO
  MotorWriting(adj_L*vL, adj_R*vR);
}// tracking
