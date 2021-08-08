import csv

import Register
import Library


class admin:

    def __init__(self,name):
        self.name = name
        self.__str__()


    def __str__(self):
        print("\n", " Management ".center(20, ' ') + "     Admin : " + self.name.capitalize(), '\n')

    def Add_Admin(self):
        while True:
            print('Whom do u want to Add?\n\t1. Admin\n\t2. User\nPress \'c\' to cancel... ',end='')
            gt = input()
            if gt in ['1','2']:
                g = int(gt)
                doo = Register.val(g)
                if doo:
                    print('Successful')
                    return True
                else:
                    print('Failed')
                    return False
            elif gt=='c':
                print('Cancelled')
                return False
            else:
                print('Invalid input')

    def Add_Books(self):

        hw = Library.add()
        if hw:
            print('Book added')
            return True
        print('Book Adding cancelled')
        return False

    def Logout(self):
        print('Bye Admin - ', self.name)
        quit(1)

    def Bor_old(self):
        ad = csv.reader(open('history.csv','r'))
        lom = []
        print(lom)
        for r in ad:
            if r:
                lom.append(r[0])
        c = 3
        while True:
            if c==0:
                break
            ml = input('Enter Borrower mail... ')
            if ml in lom:
                Library.B_History(ml)
                c = 1
                break
            elif ml.lower()=='b':
                c = 0
                break
            else:
                c-=1
                print('Borrower not found!')
                print('Press \'b\' to cancel')

        return True if c else False


    def Search_By_BookID(self):
        c = 1
        abc = 0
        while True:
            gv = input('Enter book ID... ' if abc==0 else 'Enter book ID... or Press \'w\' to cancel.. ')
            if gv=='w':
                 c = 0
                 break
            elif gv!='w':
                 adc = Library.show(gv)
                 if adc:
                     #print('Found..Task successful!')
                     eb = input('Press \'Y\' to search again or \'w\' to cancel... ')
                     if eb.upper() == 'Y':
                         abc = 1
                         pass
                     elif eb.lower() == 'w':
                         c = 0
                         break
                     else:
                         print('Invalid input')
                         c = 1
                         break

                 if not adc:
                     print('Not found!')

                     eb = input('\nPress \'Y\' to search again or \'w\' to cancel... ')
                     if eb.upper()=='Y':
                         abc=1
                         pass
                     elif eb.lower()=='w':
                         c=0
                         break
                     else:
                         print('Invalid input')
                         c=0
                         break
        if c:
            print('\nSearch Success!')
            return True
        print('\nSearch cancelled')
        return True

    def Give_book(self):
        nw = Library.give()
        if nw:
            return True
        return False

    def Book_return(self):
        ne = Library.getback()
        if ne:
            return True
        return False

    def Bor_chis(self):

        hist = Library.history()
        print()
        if hist:
            return True
        return False

    def Delete(self):
        ab = Library.delete()
        if ab:
            return True
        else:
            return False

def ask_task():
     show = {1: 'Add Admin or Bibliophile', 2: 'Borrower Current History', 3:'Borrower Old History',
             4: 'Add Books', 5: 'Search By BookID', 6: 'Remove books',
             7: 'Give a book', 8: 'Book return', 9: 'Logout'}

     for i in show:
         print(i, show[int(i)], sep='. ')
     print('Press \'q\' to quit... ',end='')
     c = 3
     while True:
         if c==0:
             print('Test me later!')
             quit(1)
         got = input()
         try:
             if int(got) in show.keys():
                 print('\nPicked task is -> ',show[int(got)])
                 return int(got)
             else:
                 c-=1
                 print('No such task')
         except ValueError:
             if got=='q':
                 print('bye!')
                 quit(1)
             else:
                 c-=1
                 print('Invalid input')



def adminpage(a):
    _tsk = {1: 'Add_Admin', 2: 'Bor_chis',3:'Bor_old',
            4: 'Add_Books', 5: 'Search_By_BookID', 6: 'Delete', 7: 'Give_book',8: 'Book_return',
            9: 'Logout'}

    while True:
        now = admin(a)
        aasked = ask_task()

        #print(aasked)
        ab = _tsk[aasked]
        class_method = getattr(admin, ab)
        result = class_method(now)

        if result:
            print('Task successful')
        else:
            print('Task incomplete')

#adminpage('nikash')