/***************************************************************************/
// File			  [node.h]
// Author		  [Erik Kuo, Joshua Lin]
// Synopsis		[Code for managing car movement when encounter a node]
// Functions  [/* add on your own! */]
// Modify		  [2020/03/027 Erik Kuo]
/***************************************************************************/

/*===========================import variable===========================*/
//int extern IRpin_LL,IRpin_L,IRpin_M,IRpin_R,IRpin_RR;
//int extern _Tp;
/*===========================import variable===========================*/

// TODO: add some function to control your car when encounter a node

int vL, vR;

bool in_the_node(int l2, int l1, int m0, int r1, int r2)  {
  int blackCount = l2+l1+m0+r1+r2;
  bool in_node_or_not = false;
  if (blackCount >= 4)  {
    in_node_or_not = true;
  }
  return in_node_or_not;
}

void left_turn()  {
  vL = 110;
  vR = 255;
  MotorWriting(vL, vR);
  delay(800);   //Needed to be modified.
}
void right_turn() {
  vL = 255;
  vR = 120;
  MotorWriting(vL, vR);
  delay(800);   //Needed to be modified.
}
void reverse_turn() {
  vL =  200;
  vR = -200;
  MotorWriting(vL, vR);
  delay(575);   //Needed to be modified.
}
void go_straight()  {
  vL = 200;
  vR = 200;
  MotorWriting(vL, vR);
  delay(600);   //Needed to be modified.
}
// here are something you can try: left_turn, right_turn... etc.
