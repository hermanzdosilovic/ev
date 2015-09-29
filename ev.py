#!/usr/bin/python

import os
import subprocess
import sys

def compile(file_name, problem_name, file_type):
    if file_type == "c":
        command = ' '.join(['gcc -ansi -Wall', file_name, '-o', problem_name])
    elif file_type == "cpp":
        command = ' '.join(['g++', file_name, '-o', problem_name])
    elif file_type == "java":
        command = ' '.join(['javac', file_name])
    else:
        command = ""

    try:
        return subprocess.check_output(
            command,
            stderr=subprocess.STDOUT,
            shell=True
        )
    except subprocess.CalledProcessError as e:
        raise Exception(e.output)


def run(file_name, problem_name, file_type):
    if file_type == "c" or file_type == "cpp":
        subprocess.call("./" + problem_name)
    elif file_type == "java":
        subprocess.call(["java", problem_name])
    elif file_type == "py":
        subprocess.call(["python", file_name])
    else:
        subprocess.call(["ruby", file_name])


def main():
    if len(sys.argv) == 1:
        print 'No file given!'
        sys.exit(1)

    argument = sys.argv[1]
    if not os.path.isfile(argument):
        print "No such file!"
        sys.exit(1)

    file_name_struct = argument.split(".")
    problem_name = file_name_struct[0]
    file_type = file_name_struct[-1]

    supported_languages = ["c", "cpp", "py", "rb", "java"]
    if file_type not in supported_languages:
        print "Language not supported"
        sys.exit(1)

    try:
        compile(argument, problem_name, file_type)
    except Exception as e:
        print e
        sys.exit(1)

    run(argument, problem_name, file_type)


if __name__ == "__main__":
    main()
