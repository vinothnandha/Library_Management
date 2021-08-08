import datetime
import re
import csv

def save(b):
    gt = csv.reader(open('data.csv','r'))
    ft = []
    for r in gt:
        if r:
            ft.append(r)
    ft.append(b)
    sv = csv.writer(open('data.csv','w',newline=''))
    sv.writerows(ft)
    return True

def dup(d,w):
    a = True
    rd = csv.reader(open('data.csv','r'))
    for row in rd:
        if row:
            if row[0] == str(w) and d == row[1]:
                a = False
    return True if a else False

def dupnum(d):
    ck = 1
    rd = csv.reader(open('data.csv','r'))
    for row in rd:
        if row:
            if row[3]==d:
                ck=0

    return True if ck else False

def dupmail(d):
    ck = 1
    rd = csv.reader(open('data.csv','r'))
    for row in rd:
        if row:
            if d.lower() == row[4]:
                ck = 0
    return True if ck else False


class checker:

    def __init__(self,value):
        self.v = value
    def name_check(self):
        now = self.v
        if now.isalpha() is not True:
            print(' No numbers / symbols allowed ')
            return 0 , 0
        elif len(now)<3:
            print('Name must be three letters long!!')
            return 0 , 0
        else:
            return now.capitalize() , 1

    def birth(self):
        ab = self.v
        ab = ab.rstrip()
        dte = ab.split('-')
        #print(dte)
        try:
            if int(dte[2])>1950:
                if datetime.date(year=int(dte[2]),month=int(dte[1]),day=int(dte[0])):
                #print(d)
                    return ab,1
            else:
                print('Invalid year')
                return 0,0
        except TypeError:
            print('Invalid date')
            return 0, 0
        except ValueError:
            print('InValid date')
            return 0,0

def val(d):
    print('\n'+'  Registration page  '.center(30,'~')+'\n')
    __detail = [0 if str(d) == '0' else 1]
    while True:
        name = input('Enter Full Name... ')
        if name=='q':
            return 0
        ask = checker(name)
        a = ask.name_check()
        if a[1]==1:
            __detail.append(a[0])
            break

    while True:
        #print('\nDOB in format "DD-MM-YYYY" ')
        dob = input('\nEnter DOB in format "DD-MM-YYYY"... ')
        if dob=='q':
            return 0
        ask = checker(dob)
        a = ask.birth()
        if a[1]==1:
            __detail.append(a[0])
            break

    while True:
        num = input('\nEnter Mobile No. ... ')
        if num=='q':
            return 0
        elif num.isnumeric() is False:
            print('Enter number alone... ')
        elif num.isnumeric() and len(num)==10:
            af = dupnum(num)
            if af:
                __detail.append(int(num))
                break
            else:
                print('Mobile number already registered!')
        else:
            print('Only 10 digits allowed!')

    while True:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,3}\b'
        mail = input('\nEnter mail-ID... ')
        if mail=='q':
            return 0
        if re.search(regex, mail):
            aj = dupmail(mail)
            if aj:
                __detail.append(mail)
                break
            else:
                print('Email already registered!')
        else:
            print("Invalid Email")

    while True:
        pwd = input('\nEnter password... ')
        if pwd=='q':
            return 0
        if len(pwd)<10:
            print('Enter password atleast 10 characters long!')
            pass

        elif re.search(r'[A-Z]', pwd) and re.search(r'[a-z]',pwd) or re.search(r'[0-9]',pwd) or re.search(r'[@#%&=$^]',pwd):
            cb = 2
            while cb:
                cnfrm = input('Confirm password... ')
                if cnfrm.rstrip()==pwd.rstrip():
                    __detail.append(pwd)
                    save(__detail)
                    __detail.clear()
                    #print(__detail)
                    return 1

                else:
                    if cb==0:
                        print('\n\nTry new password...')
                        break

                    cb-=1
                    print("Password's dont match!..Try again")
        else:

            print('Add numbers, letters and symbols in your password!')



