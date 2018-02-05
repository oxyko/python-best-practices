'''
Problem: writting a python program that runs a system call.
Note: Assuming a Unix-based OS here.
Caution: Systems differ, even running Linux you can have bash, or csh, etc. So be careful with what kind of
        system calls you're using.
'''
import subprocess


def system_call():
    '''
    Best practice: use subprocess, instead of system.os. Benefits:
        - Easy to retrieve results from the process
        - Faster
        - Easier to format the command string (esp. for special characters like ;)
    '''
    cmd = 'ls'
    output = subprocess.run(cmd, shell=True, check=True)
    print(output)