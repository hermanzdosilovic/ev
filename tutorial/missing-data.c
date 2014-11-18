/*
Run ev and see what will happen.
You will get following output:
 - missing-data.c -
* test/missing-data/missing-data.1.in:
ACCEPTED

* test/missing-data/missing-data.2.in:
25

Our task was to output length of some given string. Check out our input/output
data for this task.

As you can see our missing-data.2.out is empty. What does this mean? So, first I
will explain you what happens with rule number 1 i.e. missing-data.1.in and
missing-data.1.out. Your program missing-data.c was compiled and run and your
program got data from missing-data.1.in file. ev is smart enough to know that
there is something in missing-data.1.out, so it knows what is the correct
answer. That is why ev knows that your answer is "ACCEPTED". Because it knows
what answer you should output and what is the answer you outputed. It then
compares your answer with "correct one" and sees it they match.

But what about rule number 2? Well answer to that question is simple. ev does
not know with that to compare your results, so it just output you results to
the screen.

Try fill the missing-data.2.out with something and see what will happen.

Proceed with no-input.c
*/

#include <stdio.h>
#include <string.h>

char s[201];

int main(void) {
  scanf("%s", s);
  printf("%d\n", (int) strlen(s));
  return 0;
}
