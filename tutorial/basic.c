/*
Let me show you how does last modification time search works.

Follow these instructions:
1. Delete next line
------------- DELETE THIS LINE -------------
2. Save file
3. Run ev from your terminal

ev's output you should get looks like this:
 - basic.c -
* created test/basic/
* created test/basic/basic.1.in
* created test/basic/basic.1.out
* created test/basic/basic.2.in
* created test/basic/basic.2.out

What happened here? Well, ev knows what is the last modified file in your
working directory (it looks for .c, .cpp, .py or .rb file). When it finds one
it looks for directory test/<name of your program>/. In this case that would be
test/basic/ directory. If it does not exist, ev will create it for you.

After all that directory thing that I described, ev looks in directory
test/basic/ and tries to find some testdata. What is testdata? There are two
types of data that ev knows about:

Input data - this is the data that your program will get when it starts.
Every input data file has extension .in
And every input data has its name <name of your program>.<identifier>.in
Here <name of your program> is "basic". And identifiers are numbers.

Output data - this is the data that your program should output.
Every output data file has extension .out
And every output data has its name <name of your program>.<identifier>.out
Here <name of your program> is "basic". And identifiers are numbers.

So, for basic.1.in as input your program should output basic.2.out. To explain
you this i have prepared another example. Check out my-add.c file.

Oh, before you go there (on file my-add.c). You can try to run ev again and see
what will happen. I will explain it later. If you want to try it make sure that
this is the last modified file in this directory. ev's output will be:
 - basic.c -
* test/basic/basic.1.in:
ev: file empty and skipped

* test/basic/basic.2.in:
ev: file empty and skipped

*/

#include <stdio.h>

int main(void) {
  printf("hello, world\n");
  return 0;
}
