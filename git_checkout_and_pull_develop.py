# Loading the libraries
import os

git_checkout_develop = "git checkout develop"
git_pull_develop = "git pull origin master"
# git_command_pull_master = "git pull origin master"

# TODO: read these directory names using a config file
# config file can also be striclty a JSON file. Where
# an array of diretory names will be declared and this script
# reads all names and fills into following variable.

# directory name's in list
git_repos = [
    "boot-healthpolecore",
    "boot-social-core",
    "boot-doctors-social",
    "boot-dentists",
    "boot-module-doctor",
    "boot-module-association-admin",
    "boot-module-messsaging",
    "boot-android-asso-admin",
    "boot-module-association",
    "boot-module-groups",
    "boot-module-marketplace",
    "hp-auth",
    "boot-image-editor",
    "boot-superrecyclerview"
]

for i in git_repos:
    # change directory
    os.chdir(i)
    # TODO: Currently this gets a absolute path of the directory.
    # change this to get only the name of the directory.
    working_dir = os.getcwd()
    print("\n-----------------------" + working_dir + "-----------------------")
    print("\n=='" + git_pull_develop + "' into ==> " + working_dir)
    os.system(git_checkout_develop)        # checkout correct branch
    os.system(git_pull_develop)            # Pull the code into working directory
    # Change the directory path to previous directory
    os.chdir("..")