import os 
import subprocess
from subprocess import Popen,PIPE,call

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#To listout the only directory name
os.system("ls -d */")

userInputDirectoryName = input(bcolors.BOLD + bcolors.WARNING + "Enter the directory name to enter into it:->  " + bcolors.ENDC)

#subprocess.call('cd ' + userInputDirectoryName, shell=True)
#Popen(["cd",(userInputDirectoryName)],stdout=PIPE)
os.chdir(userInputDirectoryName)
print(os.getcwd())
os.system('git branch')
#os.system("ls")
#working_dir = os.getcwd()