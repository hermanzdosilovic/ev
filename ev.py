#!/usr/bin/python

#
#   Smart Evaluator for Competitive Programming written in Python 2
#

#
# Version: 0.9 Beta
# Date: April, 18. 2015. 
# Latest update: /
# Created by: Filip Karlo Dosilovic
# 

#
# Before official release add the following features:
#  a) input and outfiles should not depend on format
#  b) don't display warrnings generated by subprocess
#  c) clean code
#  d) add memory usage and time limit parameters 
# 

import os
import sys
import subprocess

# Default compiler for C
C = "gcc"

#Default compiler for C++
CPP = "g++"

# Function returns task name
def get_task_name():
    return str(sys.argv[1])

# Function returns directory of script
def get_main_dir():
    return os.path.dirname(os.path.realpath(__file__))

# Function returns true if the file is written in C !!!!!!!
def is_written_in_C(main_dir, task_name):
    return os.path.exists(main_dir + "/" + task_name + ".c")

# Compiles the C/C++ source code
def compile_task(cmd):
    FNULL = open(os.devnull, "w")
    p = subprocess.Popen(cmd, stdout=FNULL, stderr=subprocess.STDOUT)
    p.wait()
    #FNULL.close()
    
    
# Run compiled C/C++ file:
def run_task(task_dir, task_name):
    for i in range(1, 41):
        
        try:
            test_data_in = open(task_dir + "/" + task_name + ".in.{}".format(i))
        except:
            continue
            
        user_data_out = open(task_dir + "/" + task_name + ".user." + "out.{}".format(i), "w")
        
        p = subprocess.Popen("./" + task_name, stdin=test_data_in, stdout=user_data_out)
        p.wait()
        user_data_out.flush()

# Functions evaluates the output
def check_output(task_dir, task_name):
    for i in range(1, 41):
        
        try:
            user_data_out = open( task_dir + "/" + task_name + ".user." + "out.{}".format(i))
        except:
            continue
            
        official_data_out = open( task_dir + "/" + task_name + ".out.{}".format(i))
        
        print( "\n" + task_name + ".out.{}".format(i) + ": " )
        
        ok = True
        for (user, off) in zip(user_data_out, official_data_out):
            user_out = str(user).strip()
            off_out = str(off).strip()
            
            if not (user_out == off_out): 
                print("Wrong Answer!")
                ok = False
                break
                
        if ok:
            print("Accepted!")
        
        user_data_out.close()
        official_data_out.close()
   
   
    print("\n\n")

def delete_user_output(task_dir, task_name):
    
    for i in range(1, 41):
        try:
            user_data_out = task_dir + "/" + task_name + ".user." + "out.{}".format(i)
            os.remove(user_data_out)
        except:
            continue
    

#
#   Main function for the Evaluator
#
def main():

    # Get task name
    task_name = get_task_name()
    
    # Look for folder test in parent directory of pev.py
    main_dir = get_main_dir()
       
    # Creates string with test directory
    test_dir = main_dir + "/test"
    
    # Creates string with task directory
    task_dir = test_dir + "/" + task_name
    
    # Check to see if folder test exists
    # If the folder doesn't exits, create one, create test files for task in format:  
    # taskname.in.number and taskname.out.number
    if os.path.exists(test_dir) == False:
    
        print("Folder test doesn't exists.")
        print("Creating folder test ...")
        os.makedirs(test_dir)
        print("Creating test data ...")
        os.makedirs(task_dir)
        for i in range(1, 3):
            test_data_in = task_dir + "/" + task_name + ".in.{}".format(i)
            test_data_out = task_dir + "/" + task_name + ".out.{}".format(i)
            
            # Use better approach <----------------------------
            fp = open(test_data_in, "w+")
            fp.close()
            
            fp = open(test_data_out, "w+")
            fp.close()
            
        sys.exit(0)
    
    # Check extensions and then compile
    if is_written_in_C(main_dir, task_name):
        compile_task( cmd = [C, "-O2", task_name + ".c", "-o", task_name] )
    else:
        compile_task( cmd = [CPP, "-O2", task_name + ".cpp", "-o", task_name] )
        
    # Runs compiled source to get user output
    run_task(task_dir, task_name)
    
    # Compare output lines
    check_output(task_dir, task_name)
    
    # Delete user files
    delete_user_output(task_dir, task_name)

if __name__ == "__main__": main()

