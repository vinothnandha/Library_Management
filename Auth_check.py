import adminhome
import safebox
import userhome

def valid(v):
    print("\n",(' Admin Login ' if v==1 else " User Login").center(30,('x'if v==1 else '-')),"\n")
    if v!=1:         #user login
        print('\n1. New  Registration\n2. Login')
        while True:
            use = input('\nEnter a choice... ')
            try:
                if use in ['1','2']:
                    if use=='1':
                        pass
                        #register()
                    else:
                        break
                elif use=='q':
                    print('Bye')
                    quit(1)
                else:
                    print("Pick 1 or 2 or 'q' to quit ")
            except ValueError:
                print("Enter valid option")


    count = 4
    while count:
        if count==1:
            print("Limits reached!..Blocked")
            quit(1)
        user = input('Admin name : 'if v==1 else 'User mail : ')
        pwd = input('Password : ')
        go = safebox.check(user,pwd,v)
        now = go.verify()
        #print(now)
        if now[0] == 1:
            count = 0
            print("Hi Admin" if v==1 else 'Hi User',now[1])
            adminhome.adminpage(now[1]) if v==1 else userhome.user(now[1])
            break
        elif now[0]==404:
            count-=1
        else:
            print("Password wrong! ", count-1, " Attempts left!!")
            count-=1

    #admin_ryt()


def User():
    print("\n","Reader Login".center(40,'-'),"\n")
    cnt = 4
    while cnt:
        if cnt == 1:
            print("Limits reached!..Blocked")
            quit(1)
        user = input('User : ')
        pwd = input('Password : ')
        go = safebox.check(user, pwd,1)
        now = go.verify()
        # print(now)
        if now[0] == 1:
            count = 0
            print("Hi User", now[1])
            break
        elif now[0] == 404:
            print("Incorrect user name!")
        else:
            print("Password wrong! ", cnt - 1, " Attempts left!!")
            cnt -= 1