/*
Modify this file and run ev. See what happened.

If the first character in .out file is '$' then ev wont compare your results.
Your output will be presented to you thru terminal. This is usefull when you
want to debug your program.

Try to remove '$' from .out files and see what will happen.

Proceed with tle.c
*/

#include <stdio.h>

int main(void) {
  int a, b;
  scanf("%d%d", &a, &b);
  printf("%d\n", a&b);
  return 0;
}
