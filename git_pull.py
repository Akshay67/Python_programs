""""
This file is used for pull the code from your repos;
Just save this file in the directory where your all repositories are present and
put the repos name in git_repos list;
And just run this script and pull all code from remote repo to your local machine
"""

# Loading libraries
import os

# Repository name's in list
git_repo = ["Put your repos name's only one by one"]

# This for loop will run one by one list element
# It visit one by one repos and pull the code form origin to local machine
for i in git_repo:
    os.chdir(i)                                 # changing the directory
    working_dir = os.getcwd()
    print("\n Current directory:"+working_dir)
    print("\n Pulling into: "+working_dir)
    os.system('git pull origin develop')        # Pull the code into local working directory from origin
    print("\n Back to previous directory")
    os.chdir("..")                              # Change the directory path to previous directory
    print("\n Previous directory is: " + os.getcwd())
