import sambox
import Register
import userhome
import adminhome


def validate_login(a,b):
    now = sambox.Check(a.capitalize(),b)
    he = now.name_check()
    #print(he,he[0],he[1],a,sep='')
    if not he:
        print('Back to Home...')
        start()
    else:
        print('Login Successful')
        aa = userhome.user(a,he[1]) if b==2 else adminhome.adminpage(a)
        if aa is False:
            start()

def login(w):
    print(" Admin Login ".center(30,'-') if w==1 else ' User Login '.center(30,'*'))
    c = 3

    if w==2:         #for users
        while True:
            try:
                reg = input('\n\t1. Login\n\t2. Register\nPress \'q\' to quit!\n\nPick one... ')
                if reg not in ['1','2','q']:
                    print("Choose or press 'q' to exit...")
                elif reg=='q':
                    print("Bye user")
                    quit(1)
                elif reg=='2':
                    bck = Register.val(0)
                    #print(bck)
                    if bck==1:
                        print('Registered Successfully!\n...Wanna login?... Y(yes) / N(no).. ',end='')
                        lg = input()
                        start() if lg=='y'.lower() else quit(1)
                    else:
                        print('Registration cancelled..!')
                        quit(1)
                elif reg=='1':
                    break



            except ValueError:
                if c==0:
                    print('Vyee')
                    quit(1)

                print('Invalid')

    #for Admin
    while True:
        if c==0:
            print('Test me later...Bye')
            quit(1)

        a = input('Admin name... 'if w==1 else 'User Email... ')
        if  a == 'q':
            print('Quitting..Bye!')
            quit(1)


        elif len(a)<3:
            print('Invalid characters!')

        elif a!='q' and len(a)>=3:
            ak = Register.dup(a,w)
            if w==1 and not ak:
                #print('Admin present')
                validate_login(a,w)

            elif w==2 and ak:
                #print('User present')
                validate_login(a,w)
            else:
                c-=1
                print(('Admin ' if w == 1 else 'User Email ') + a + ' not Present')



        else:
            print('Invalid characters' if a.isalpha()==0 else 'Too short name')
            c-=1


if __name__ == '__main__':

    def start():
        print(' Welcome to Library '.center(50))
        d=3
        while True:
            if d==0:
                print("Logging out...")
                quit(1)
            who = input('\n1. Admin\n2. Bibliophile\nPress \'q\' to quit!\n\nWho are you... ')
            try:
                if int(who) in [1, 2]:
                    print("Hi ", 'Admin' if int(who) == 1 else 'User')
                    login(int(who))
                    break
                else:
                    print('Enter 1 or 2 or (\'q\') to exit')
            except ValueError:
                if who == 'q':
                    print("Come back later")
                    quit(1)
                d-=1
                print("Invalid input")
    start()

