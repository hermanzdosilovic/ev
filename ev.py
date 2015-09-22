#!/usr/bin/python

import os
import subprocess
import sys


def compile(file_name, problem_name, file_type):
    command = ""
    if file_type == "c":
        command = ' '.join(['gcc', file_name, '-o', problem_name])
    elif file_type == "cpp":
        command = ' '.join(['g++', file_name, '-o', problem_name])
    elif file_type == "java":
        command = ' '.join(['javac', file_name])

    try:
        subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError:
        sys.exit(1)


def run(file_name, problem_name, file_type):
    if file_type == "c" or file_type == "cpp":
        subprocess.call("./" + problem_name)
    elif file_type == "java":
        subprocess.call(["java", problem_name])
    elif file_type == "py":
        subprocess.call(["python", file_name])
    elif file_type == "rb":
        subprocess.call(["ruby", file_name])
    else:
        pass

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

compile(argument, problem_name, file_type)
run(argument, problem_name, file_type)
