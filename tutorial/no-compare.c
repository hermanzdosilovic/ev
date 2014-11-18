/*
Modify this file and run ev. See what happened.

If the first character in .out file is '!' then ev wont compare your results.
Your output will be saved in .user.out file. This is usefull when you want to
debug your program and you have a large output.

Try to remove '!' from .out files and see what will happen.

Proceed with to-console.c
*/

#include <stdio.h>

char s1[201], s2[201];

int main(void) {
  scanf("%s%s", s1, s2);
  printf("%s+%s\n", s1, s2);
  return 0;
}
