import csv

def _check_mail(a):
    with open('data.csv','r') as f:
        rd = csv.reader(f,delimiter=',')
        for row in rd:
            if row:
                if row[0]=='0' and a.lower()==row[4].lower():
                    f.close()
                    return row
        f.close()
        return False

def _phcheck(a):
    try:
        int(a)
    except TypeError:
        return False


    with open('data.csv','r') as f:
        rd = csv.reader(f,delimiter=',')
        #cnt = 0
        for row in rd:
            if row:
                if row[0]=='1' and str(a)==row[3]:
                    f.close()
                    return row[-1]
        f.close()
        return False

class Check:

    def __init__(self,now,then):
        self.name = now
        self.who = then
        #print(self.name,self.who,sep=' == ')

    def name_check(self):
        if self.who==1:
            __ph = input('Enter phone number... ')
            adpwd = _phcheck(__ph)
            if adpwd:
                c=3
                while True:
                    if c == 0:
                        print('Blocked..!')
                        return 0

                    wd = input('Enter your Admin password.. ')
                    if wd == adpwd:
                        print('password correct')
                        return 1
                    else:

                        print('Wrong password...', c, ' attempts left!')
                        c -= 1
            else:
                print('Not present')
                return 0


        elif self.who==2:
            #print('Checking mail...')

            __pd = _check_mail(self.name)
            #print(__pd)
            c = 3
            while True:
                if c==0:
                    print('Blocked..!')
                    return 0,0

                ad = input('Enter your password.. ')
                if ad==__pd[5]:
                    nm = __pd[1]
                    #print(nm)
                    #print('password correct')
                    return 1,nm
                else:
                    print('Wrong password...',c,' attempts left!')
                    c-=1