import csv
import datetime

import Library

class Bibliophile:
    def __init__(self,m,n):
        self.mail = n
        self.name = m
        #print(self.name,self.mail)
        self.__str__()

    def __str__(self):
        print("\n", " Home ".center(20, ' ') + "     User : " + self.name.capitalize(), '\n')

    def Logout(self):
        print('Bye User - ', self.name)
        quit(1)

    def C_borrow(self):
        br = Library.mail_hist(self.mail)
        if br:
            return True
        return False

    def Book_Details(self):
        br = Library.mail_hist(self.mail)
        bks = Library.get_my_books(self.mail)
        if not bks:
            print('No books in holdings!')
            return True
        c = 3
        while True:
            if c==0:
                break
            ml = input('Enter the Book ID... ')
            if ml=='w':
                c=0
                break
            elif ml.upper() in bks:
                Library.show(ml)
                c = 1
                break
            else:
                c-=1
                print('Invalid Book ID!')

        return True if c else False

    def head(self,w):
        if w==0:
            return False

        print('\n'+'-'*80)
        print('Book ID','Buy Date','Return Date','Days','Fine',sep='       ')
        print('-'*60)


    def bal(self,buy,gve):
        fin = ''

        fd = buy.split('-')
        ld = gve.split('-')

        y1,y2 = int(fd[0]) , int(ld[0])
        m1,m2 = int(fd[1]),int((ld[1]))
        d1,d2 = int(fd[2]),int(fd[1])

        a = datetime.date(year=y1,month=m1,day=d1)
        b = datetime.date(year=y2,month=m2,day=d2)

        dif = (a-b).days
        if dif>15:
            py = round((dif/14)*100)
            fin = str(dif).center(10)+str(py).center(10)
        else:
            fin = ' - '.center(10) + ' NA '.center(10)

        return fin

    def B_History(self):
        ab = csv.reader(open('old.csv','r'))
        f = 1
        for a in ab:
            if a:
                #print(a,self.mail)
                if a[0]==self.mail.lower() and len(a)>1:
                    self.head(f)
                    for v in a[1:]:
                        f = 0
                        gt = v.split('@')
                        bid = gt[0]
                        bl = str(gt[1]).split('$')
                        gve , buy =bl[1], bl[0]
                        print(bid.center(7),buy,gve,self.bal(buy,gve),sep='      ')

                else:
                    pass
        print()
        return False if f else True

def asked():
    sh = {1: 'My Books', 2:'My Book Details',3:'Borrowed History',4:'Logout'}
    for i in sh:
        print(i, sh[int(i)], sep='. ')
    print('Press \'q\' to quit... ', end='')
    c = 3
    while True:
        if c == 0:
            print('Test me later!')
            quit(1)
        got = input()
        try:
            if int(got) in sh.keys():
                print('\nPicked task is -> ', sh[int(got)])
                return int(got)
            else:
                c -= 1
                print('No such task')
        except ValueError:
            if got == 'q':
                print('bye!')
                quit(1)
            else:
                c -= 1
                print('Invalid input')


def user(ml,nm):
    #sh = {1: 'My Books', 2:'My Book Details',3:'Borrowed History',4:'Logout'}
    _use = {1:'C_borrow' , 2:'Book_Details',3:'B_History',4:'Logout'}

    while True:
        now = Bibliophile(ml,nm)
        aasked = asked()
        ab = _use[aasked]
        class_method = getattr(Bibliophile, ab)
        result = class_method(now)

        if result:
            print('Task successful')
        else:
            print('Task incomplete')



