import csv


def _asafe():
    _f = csv.reader(open('data.csv','r'))
    dictt = {}
    for line in _f:
        if line and line[0]=='1':
            #print(line)
            u, p = line[1] , line[5]
            dictt[u]=p

    #print(dictt)
    return dictt

#_asafe()

def _usafe():
    _f = csv.reader(open('data.csv', 'r'))
    dictt = {}
    for line in _f:
        #print(line)
        if line and line[0]=='0':
             u, p = line[4], line[5]
             dictt[u] = p
    #print(dictt)
    return dictt


def _add(a,b):
    with open('Register.py', 'a+') as f:
        f.seek(0)
        data = f.read(100)
        if len(data)>100:
            f.write('\n')
        f.write(a+","+b)
        f.close()



class check:
    __admin = _asafe()
    _users = _usafe()
    def __init__(self,n,p,ua):
        self.name = n
        self.p = p
        self.s = ua

    def bd(self):
        _add(self.name,self.p)

    def _dd(self):
        pass

    def verify(self):
        if self.name=='admin':
            return [1,'admin']


        if self.s==1:
            print(self.__admin.keys())
            if self.name in self.__admin.keys():
                # print("User present")
                if self.p == self.__admin[self.name]:
                    # print("Password ok !")
                    return [1, self.name]
                elif self.p != self.__admin[self.name]:
                    # print("Password wrong")
                    return [0, 0]
            else:
                print("Admin not found ")
                return [404, 0]

        elif self.s==2:
            if self.name in self._users.keys():
                # print("User present")
                if self.p == self._users[self.name]:
                    # print("Password ok !")
                    return [1, self.name]
                elif self.p != self._users[self.name]:
                    # print("Password wrong")
                    return [0, 0]
            else:
                print("User not found")
                return [404, 0]

