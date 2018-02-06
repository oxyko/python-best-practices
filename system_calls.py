'''
Goal: Invoke a shell command from python code.
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
    try:
        output = subprocess.check_output('ls -a', shell=True)
        print("Output is: ")
        print(output)

        # Note that without shell=True, the exception is not going to be caught
        output = subprocess.check_output(['ls', '-al'])
        print("\nOutput is: \n{}".format(output))

    except subprocess.CalledProcessError as e:
        print("Caught an exception, while executing a subprocess.check_output: ")
        print(e)

if __name__ == '__main__':
    system_call()