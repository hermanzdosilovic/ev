import signal
import timeit
import os
import time
import multiprocessing
import subprocess
import atexit
import sys

ON_WINDOWS = (sys.platform == 'win32')
TIMEOUT = 1
TIMEOUT_OFFSET = 0.5
DEFAULT_INT = -1
WA = 0
AC = 1
TLE = 2

def run_program(child_pid, time_taken, program_name):
    prog = subprocess.Popen(['./' + program_name])
    child_pid.value = prog.pid
    start_time = timeit.default_timer()
    prog.wait()
    time_taken.value = timeit.default_timer() - start_time
    return

def start_test(program_name):
    child_pid = multiprocessing.Value('i', DEFAULT_INT)
    time_taken = multiprocessing.Value('d', DEFAULT_INT)
    run_process = multiprocessing.Process(target=run_program, args=[child_pid, time_taken, program_name])
    run_process.start()
    run_process.join(TIMEOUT + TIMEOUT_OFFSET)
    is_tle = run_process.is_alive()
    if run_process.is_alive() == True: 
        run_process.terminate()
        if child_pid.value != -1:
            os.kill(child_pid.value, signal.CTRL_BREAK_EVENT if ON_WINDOWS else signal.SIGTERM)
    
    if time_taken.value != DEFAULT_INT:
        is_tle = time_taken.value > TIMEOUT
    ac = AC
    return TLE if is_tle else ac  

result = start_test('a.out')
print result
