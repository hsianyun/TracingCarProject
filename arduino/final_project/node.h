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
    send_msg("I am in the node, what should I do?");
  }
  return in_node_or_not;
}

void left_turn()  {
  vL = 130;
  vR = 255;
  MotorWriting(vL, vR);
  delay(1000);   //Needed to be modified.
}
void right_turn() {
  vL = 255;
  vR = 130;
  MotorWriting(vL, vR);
  delay(1000);   //Needed to be modified.
}
void reverse_turn() {
  vL =  200;
  vR = -200;
  MotorWriting(vL, vR);
  delay(1000);   //Needed to be modified.
}
void go_straight();
// here are something you can try: left_turn, right_turn... etc.
