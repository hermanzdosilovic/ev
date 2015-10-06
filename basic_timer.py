import ctypes
import signal
import timeit
import os
import time
import multiprocessing
import subprocess
import atexit
import sys

ON_WINDOWS = (sys.platform == 'win32')
WA = 0
AC = 1
TLE = 2

class Result:
    WA = 0
    AC = 1
    TLE = 2
    def __init__(self, status, time):
        self.status = status
        self.time = time

class Tester:
    DEFAULT_INT = -1
    
    def __init__(self, timeout, timeout_offset):
        self.timeout = timeout
        self.timeout_offset = timeout_offset

    def run_program(self, child_pid, time_taken, command, in_file, out_file):
        input_file = open(in_file, 'r')
        output_file = open(out_file, 'w')
        start_time = timeit.default_timer()
        prog = subprocess.Popen(args=[command], stdin=input_file, stdout=output_file)
        child_pid.value = prog.pid
        prog.communicate();
        time_taken.value = timeit.default_timer() - start_time
        return

    def kill(self, pid):
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.OpenProcess(1, 0, pid)
        return (0 != kernel32.TerminateProcess(handle, 0))

    def start_test(self, command, in_file, out_file, user_out):
        child_pid = multiprocessing.Value('i', self.DEFAULT_INT)
        time_taken = multiprocessing.Value('d', self.DEFAULT_INT)
        run_process = multiprocessing.Process(target=self.run_program, args=[child_pid, time_taken, command, in_file, user_out])
        run_process.start()
        run_process.join(self.timeout + self.timeout_offset)
        is_tle = run_process.is_alive()
        if run_process.is_alive() == True: 
            run_process.terminate()
            if child_pid.value != -1:
                if ON_WINDOWS:
                    kill(child_pid.value)
                else:
                    os.kill(child_pid.value, signal.SIGTERM)
        
        if time_taken.value != self.DEFAULT_INT and time_taken.value > self.timeout or time_taken.value == self.DEFAULT_INT:
            return Result(Result.TLE, time_taken.value)
        #usporedi out_file i user_out
        ac = AC
        return Result(ac, time_taken.value)

tester = Tester(1, 0.5)
result = tester.start_test('./a.out', './in.txt', './out.txt', './user.txt')
print str(result.status) + " " + str(result.time)
