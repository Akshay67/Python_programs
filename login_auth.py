'''
def storeUserDetails(username,password):
    with open('userdeatil.txt','w') as f:
        f.write("username- {}\npassword- {}".format(username,password))            
'''
def loginUser(username,password):
    with open('userdeatil.txt','r') as f:
        uname = (f.readline().split('- ')[1].strip())
        passwd = (f.readline().split('- ')[1])
        
    if username == uname and password == passwd:
        print('login done..!')
    else:
        print('login failed..!')

def userRegistration(username,password):
    with open('userdeatil.txt','w') as f:
        f.write("username- {}\npassword- {}".format(username,password))
    print("Congratulation Your account has been created successfully.")            

choice = input("Do you have already account to login: Y/N -> ")

if choice =='Y' or 'y':
    cmdUsername = input("Enter the username: ")
    cmdPassword = input("Enter the password: ")
    loginUser(cmdUsername,cmdPassword)

elif choice == 'N' or 'n':
    cmdUsername = input("Please Enter the username to create account: ")
    cmdPassword = input("PLease Enter the password to create account: ")
    userRegistration(cmdUsername,cmdPassword)
else:
    print("Something went wrong.!")


#storeUserDetails(cmdUsername,cmdPassword)
#getUserDetails()
#nloginUser(cmdUsername,cmdPassword)

'''
def getUserDetails():
    with open('userdeatil.txt','r') as f:
        getUserDetails.uname = (f.readline().split('- ')[1])
        getUserDetails.passwd = (f.readline().split('- ')[1])
    return (getUserDetails.uname,getUserDetails.passwd)
    #print(getUserDetails.uname)
    #print(getUserDetails.passwd)
'''
