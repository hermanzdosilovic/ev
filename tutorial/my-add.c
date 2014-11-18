/*
Modify this file and save it. You can delete next line to do that.
------------- DELETE THIS LINE -------------

Run ev and see what happend. You got this output:
 - my-add.c -
* test/my-add/my-add.1.in:
ACCEPTED

* test/my-add/my-add.2.in:
ACCEPTED

Lets first take a look what do we have in my-add.1.in and my-add.1.out file
my-add.1.in:
2 2

my-add.1.out:
4

As you can see from our C code bellow we can say that our task was to add
two numbers that we got from user. And what are these .in and .out files?
Well, those are our tests. We can say that those are our RULES. And the rule for
test 1 means:
If you get 2 and 2 as input, you should output 4. If you output 4 your answer
will be accepted.

Lets see our second rule i.e. files my-add.2.in and my-add.2.out.
If you get 10 and 40 as input, you should output 50. If you output 50 your
answer will be accepted.

Try to modifiy our code. For example calculate a * b instead of a + b and see
what happens.

Please proceed with file missing-data.c
*/

#include <stdio.h>

int main(void) {
  int a, b;
  scanf("%d%d", &a, &b);
  printf("%d\n", a + b);
  return 0;
}
