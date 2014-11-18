/*
Modify this file and run ev. See what happened.

TLE means "time limit exceeded". ev will report status tle if your program
is running more than 1 second. Time that takes your program to input data is
ignored.

Delete while loop in code and see what will happen.

Proceed with colors.txt
*/

#include <stdio.h>

int main(void) {
  int a, b;
  scanf("%d%d", &a, &b);
  printf("%d\n", a + b);
  while(1) continue;
  return 0;
}
