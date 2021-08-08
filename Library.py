
import csv
import random
import datetime
import Register

def get_my_books(m):
    c = False
    a = csv.reader(open('history.csv','r'))
    ab = []
    for row in a:
        if row:
            if row[0]==m.lower():
                ak = row[1:]
                if ak:
                    c = True
                    for a in ak:
                        nv = a.split('@')
                        ab.append(nv[0])
    if c:
        return ab

    return False

def upd():
    df = csv.reader(open('data.csv','r'))
    bj = csv.reader(open('history.csv','r'))

    db = []
    mls = []
    for row in bj:
        if row:
            db.append(row)
            mls.append(row[0])

    for row in df:
        if row:
            if row[4] not in mls:
                db.append([row[4]])
    fk = csv.writer(open('history.csv','w',newline=''))
    fk.writerows(db)

def dupid(fo):
    #returns False if Duplicate is present and VV
    ch = True
    ak = csv.reader(open('books.csv','r'))
    __ids = []
    for r in ak:
        if r:
            __ids.append(r[0])
    if fo.upper() in __ids:
        #print('present here')
        return False
    #print("not present")
    return True

def show(bkid):
    #print(bkid)
    c = 0
    with open('books.csv','r') as f:
        reader = csv.reader(f)
        for row in reader:
            #print(row)
            if row:
                if row[0]==bkid.upper():
                    print('\n'+' Book Details '.center(50,'~')+"\nName : {}\nAuthor : {}\nPages : {}\nStocks available : {} \nISBN : {}\nPublished year : {}".format(*row[1:]),end='\n'+'~'.center(50,'~')+'\n')
                    f.close()
                    c=1
                    break
        if c:
            return True , row
        return False

def generateid(name,year):
    d = name + str(year)
    while True:
        a = [random.choice(d) for i in range(6)]
        bid =''.join(a)
        #print(bid)
        if not dupid(bid):
            print('Already present! Trying another...')
        else:
            break
    return bid

def dubisbn(a):
    file = csv.reader(open('books.csv','r'),delimiter=',')
    for row in file:
        if row:
            return True if a==row[5] else False
    return False

def add():
    c = 3
    base = []
    #book = []
    #name
    while True:
        if c==0:
            print('Cancelled!')
            break
        name = input('Enter Book name : ')
        if len(name)<3 and name!='e':
            print('Book name is too small!\nPress \'e\' to cancel')
        elif name=='e':
            c=0
        else:
            base.append(name.capitalize())
            #print(name)
            break

    #author
    while True:
        if c==0:
            print('Cancelled')
            break
        author = input('Enter Author name : ')

        if not (author.replace(' ','')).isalpha():
            print('No number\'s allowed!\nPress \'e\' to cancel')
        elif author=='e':
            c=0
        elif len(author)<3:
            print('Author name be atleast three letters long!\nPress \'e\' to cancel')
        else:
            base.append(author.capitalize())
            #print(author.capitalize())
            break

    #pages
    while True:
        if c==0:
            print('Cancelled')
            break
        pages = input("Enter the number of pages in book... ")
        try:
            if int(pages)<5:
                print('A book should atleast have 5 pages!\nPress \'e\' to cancel')
            elif int(pages)>1000:
                print('Enter a number between 5 and 1000!\nPress \'e\' to cancel')
            else:
                base.append(int(pages))
                #print(pages)
                break

        except ValueError:
            if pages=='e':
                c=0
                pass

            print('Invalid input')

    #copies available
    while True:
        if c==0:
            print('Cancelled')
            break
        stock = input('Enter the stock available!')
        try:
            if 0<int(stock)<1000:
                base.append(int(stock))
                #print(' left ',stock)
                break
            else:
                print('Less than 0 'if int(stock)<0 else 'Should be less than 1000')
        except ValueError:
            if stock=='e':
                c=0
                pass
            print('Invalid input')

    #isbn
    while True:
        if c==0:
            print('Cancelled')
            break
        isbn = input('Enter ISBN number')
        try:
            if int(isbn) and len(isbn)==13 and isbn.isdigit():
                if not dubisbn(isbn):
                    base.append(int(isbn))
                    break
                print('ISBN Already present')
            else:
                print('ISBN should be 13 digits')

        except ValueError:
            if isbn=='e':
                c=0
                pass
            print('ISBN should not contain alphabets!')

    #year
    while True:
        ab = int(datetime.datetime.now().year)

        if c==0:
            print('Cancelled')
            break
        year = input('Enter published year.. ')
        try:
            if 1600<=int(year)<=ab:
                base.append(int(year))
                #print('Published year ',year)
                break
            else:
                print('Published year must be greater than 1600' if int(year)<1600 else 'Dont enter future year!')
        except ValueError:
            if year=='e':
                c=0
                pass
            print('No letters allowed!')


    #print(c)
    if c==0:
        print('Books not added!')
        return False

    #print(base)
    bookid = generateid(base[1],base[5])
    #print(bookid)

    details = base
    details.insert(0,bookid.upper())

    heads = ['Book ID','Book Name','Author Name','Pages','Copies available','ISBN','Year']
    with open('books.csv','a',newline='\n') as f:
        write = csv.writer(f)
        write.writerow(details)
        f.close()
    return True

def delete():
    ch = False
    r = 1
    while True:
        iid = input('Enter book ID... ')
        if iid == 'd':
            ch = True
            break

        elif len(iid)!=6:
            r=0
            print('Invalid input..ID must be 6 digit long')

        elif len(iid)==6 and not dupid(iid):
            #print(dupid(iid))
            lt = []
            lines = csv.reader(open('books.csv','r'))
            for row in lines:
                #print(row)
                if row and row[0]!=iid.upper():
                    lt.append(row)
                else:
                    ch,r=True,0
            ff = csv.writer(open('books.csv','w',newline='\n'))
            ff.writerows(lt)
            break
        elif dupid(iid):
            #print(dupid(iid))
            print('Books ID not found')
            break


    if ch and not r:
        print('Deleted')
        return True
    elif ch and r:
        print('Cancelled')
        return False
    else:
        print('Press \'d\' to cancel or..')
        delete()

def cpy(iidd):
    dd = csv.reader(open('books.csv','r'))
    cv = 0
    for row in dd:
        if row:
            if row[0] == iidd.upper():
                print('Copies left : ', row[4])
                cv = int(row[4])
    return cv

def givenow(bid):
    c = 3
    d = 0
    while True:
        if c==0:
            print('Too many tries!')
            break
        mail = input('Enter borrower mail ID : ')
        if mail.lower()=='e':
            c=0
            break
        else:
            ak = csv.reader(open('history.csv','r'))
            bp = []
            for row in ak:
                if row:
                    aki = []
                    for a in row[1:]:
                        sd = a.split('@')
                        aki.append(sd[0])
                    #print(aki)
                    if row[0].lower()==mail.lower() and bid.upper() in aki:
                        print('Book already given!')
                        d ,c = 1,0
                        #bp.append(row)
                    if row[0].lower()==mail.lower() and bid.upper() not in aki:
                        c = 1
                        now = datetime.date.today()
                        row.append(bid.upper()+'@'+str(now))
                        bp.append(row)
                    else:
                        bp.append(row)
            bpp = csv.writer(open('history.csv','w',newline=''))
            for a in bp:
                bpp.writerow(a)
            break
    if c==1 and d==0:
        return True
    if d==1 and c==0:
        print('Already Given!')
        return False
    print('Invalid mail')
    return False

def roa(gd,ua):
    bk = csv.reader(open('books.csv','r'))
    nl =[]
    for row in bk:
        if row:
            if row[0]==gd.upper():
                b = int(row[4])+1 if ua else int(row[4])-1
                row[4]=str(b)
                nl.append(row)
            else:
                nl.append(row)
    ck = csv.writer(open('books.csv','w',newline=''))
    ck.writerows(nl)
    return True

def give():
    c=3
    while True:
        if c==0:
            break
        iidd = input('Enter Book ID... ')
        if iidd.upper()=='W':
            c=0
            break
        if len(iidd)!=6:
            c-=1
            print('Book ID must be 6 letters long!')
        afs = dupid(iidd)
        if not afs:
            show(iidd)
            cp = cpy(iidd)
            if cp:
                gv = givenow(iidd)
                if gv:
                    roa(iidd,0)
                    print('Success')
                    print('Give again or Press \'w\' to cancel')

                else:
                    #print('Failure')
                    print('Try again or Press \'w\' to cancel')

            else:
                print('No copies left!')
                c=0
                break

        else:
            c-=1
            print('Book not present!')
            print('Try again or Press \'w\' to cancel')

    if c==0:
        print('Share a book next time!')
        return False

    return True

def due(a):
    now = datetime.date.today()
    a = a.split('-')
    y,m,d = int(a[0]) , int(a[1]) , int(a[2])
    a = datetime.date(year=y,month=m,day=d)
    dys = (now-a).days

    if dys>15:
        du = round((dys/14)*100)
        return str(du).center(15) + str(dys).center(15)

    else:
        return ' _ '.center(15) +  ' _ '.center(15)


def mail_hist(ml):
    print('-'*50)
    #print(ml)
    p = True
    ak = csv.reader(open('history.csv', 'r'))
    for row in ak:
        if row:
            if row[0] == ml.lower():
                first = 1
                a = row[1:]
                if len(a):
                    for i in row[1:]:
                        bi, dt = i.split('@')
                        df = due(dt)
                        if first:
                            first = 0
                            print('Book ID'.center(10), 'Bought Date'.center(10), 'Due Amount'.center(15),
                                  'Days'.center(10), '\n')
                        print(bi.center(10), dt.center(10), df)
                else:
                    print('No borrowing history')
                    p = 0
                    break
    print('-'*50)
    return True if p else False

def history():
    upd()
    ch ,c = 1,2
    ak = csv.reader(open('history.csv','r'))

    a = [r[0] for r in ak]
    print("Borrower\'s List:\n")
    for i in a:
        print(i)

    bo = ''
    while True:
        if c==0:
            ch=0
            print('Try later!')
            break
        ml = input('Enter Borrower Mail... ')
        if ml.lower()=='m':
            ch = 0
            break
        elif ml not in a:
            ch = 0
            c-=1
            print('Borrower',ml,' not found')

        else:
            bo=ml
            #print('Found',ml)
            ak = csv.reader(open('history.csv','r'))
            for row in ak:
                if row:
                    if row[0]==ml.lower():
                        first = 1
                        a = row[1:]
                        if len(a):
                            for i in row[1:]:
                                bi , dt = i.split('@')
                                df = due(dt)
                                if first:
                                    first = 0
                                    print('-' * 50)
                                    print('Book ID'.center(10), 'Bought Date'.center(10), 'Due Amount'.center(15),
                                      'Days'.center(10), '\n')
                                    print('-' * 50)
                                print(bi.center(10),dt.center(10),df)
                        else:
                            print('No borrowing history')
                            c=0
                            break

            break
    print('-' * 50)
    if c:
        return True , bo
    return False

def makehis(mle,bid):
    nd = str(datetime.date.today())
    ak = csv.reader(open('history.csv','r'))
    nb = []
    for row in ak:
        if row:
            if row[0].lower()==mle.lower():
                sv = str(bid)+'$'+nd
                #print(sv)
                for v in row[1:]:
                    #print(v)
                    if v==bid.upper():
                        a = row.index(v)
                        row.insert(a,sv)
                        row.remove(v)
                nb.append(row)
            else:
                nb.append(row)

    #for i in nb:
    #    print(i)
    up = csv.writer(open('old.csv','w',newline=''))
    up.writerows(nb)

def rmv(bid,ml):
    now = csv.reader(open('history.csv','r'))
    nw = [a for a in now]
    ad = []
    for i in nw:
        if i:
            if ml.lower() == i[0]:
                k = [ml.lower()]
                for v in i[1:]:
                    ck = v.split('@')
                    if ck[0] == bid.upper():
                        makehis(ml,v)
                        pass
                    else:
                        k.append(v)
                ad.append(k)
            else:
                ad.append(i)

    fina = csv.writer(open('history.csv','w',newline=''))
    fina.writerows(ad)

def getback():
    bks = csv.reader(open('books.csv','r'))
    bkid = [a[0] for a in bks]
    #print(bkid)
    now = history()
    #print(now)
    ml = now[1] if now else ''
    c = 3
    if now:
        while True:
            if c==0:
                print('try later')
                break
            nd = input('Enter the book ID to get back...')
            show(nd)
            if nd.upper() in bkid:
                roa(nd,1)
                rmv(nd, ml)
                c = 1
                print('Book Returned')
                break
            else:
                c-=1
                print('No such book in user account..Try again')


    if c:
        return True
    return False






#=====

def head(w):
    if w==0:
        return False
    print('\n'+'-'*80)
    print('Book ID','Buy Date','Return Date','Days','Fine',sep='       ')
    print('-'*60)


def bal(buy,gve):
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




def B_History(sel):
     ab = csv.reader(open('old.csv','r'))
     f = 1
     for a in ab:
         if a:
             #print(a,self.mail)
             if a[0]==sel.lower() and len(a)>1:
                 head(f)
                 for v in a[1:]:
                     f = 0
                     gt = v.split('@')
                     bid = gt[0]
                     bl = str(gt[1]).split('$')
                     gve , buy =bl[1], bl[0]
                     print(bid.center(7),buy,gve,bal(buy,gve),sep='      ')

             else:
                 pass
     print()
     return False if f else True












