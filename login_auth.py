cmdUsername = input("Enter the username: ")
cmdPassword = input("Enter the password: ")

def storeUserDetails(username,password):
    with open('userdeatil.txt','w') as f:
        f.write("username- {}\npassword- {}".format(username,password))            
'''
def getUserDetails():
    with open('userdeatil.txt','r') as f:
        getUserDetails.uname = (f.readline().split('- ')[1])
        getUserDetails.passwd = (f.readline().split('- ')[1])
    return (getUserDetails.uname,getUserDetails.passwd)
    #print(getUserDetails.uname)
    #print(getUserDetails.passwd)
'''
def loginUser(username,password):
    with open('userdeatil.txt','r') as f:
        uname = (f.readline().split('- ')[1].strip())
        passwd = (f.readline().split('- ')[1])
        
    if username == uname and password == passwd:
        print('login done..!')
    else:
        print('login failed..!')


#storeUserDetails(cmdUsername,cmdPassword)
#getUserDetails()
loginUser(cmdUsername,cmdPassword)