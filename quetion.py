
class don ():
    def shagul (self ,c,g,h):
        return c+g+h
    def sathish (self,a,b,c):
        return a+b+c
yy=  don ()
print(yy.shagul(1,2,3))
# print(yy.sathish(3,4,6))


class gun ():
    def dance (self,a,b):
        c=a+b
yy = gun()
print (yy.dance(10,13))


class friuts ():

    def mango (self,prize,kilo):
        return prize *kilo
    def orange (self,prize,kilo):

        return prize *kilo
    def papaya (self,prize,kilo):

        return prize * kilo
balance=1000
yy= friuts()
mangoprize = yy.mango(6,10)
orangeprize=yy.orange(5,8)
papayaprize=yy.papaya(7,10)
print(balance-mangoprize-orangeprize-papayaprize)



class friuts ():

    def mango (self,prize,kilo):
        return prize *kilo
    def orange (self,prize,kilo):

        return prize *kilo
    def papaya (self,prize,kilo):

        return prize * kilo
balance=int(input("enter the balance available"))
mprice=int(input("enter the m price"))
oprice=int(input("enter the o price"))
pprice=int(input("enter the p price"))
mkg=int(input("enter the m kg"))
okg=int(input("enter the o kg"))
pkg=int(input("enter the p kg"))
yy= friuts()
mangoprize = yy.mango(mprice,mkg)
orangeprize=yy.orange(oprice,okg)
papayaprize=yy.papaya(pprice,pkg)
print("Mango price",mangoprize)
print("orange price",orangeprize)
print("papaya price",papayaprize)
print("Remaining",balance-mangoprize-orangeprize-papayaprize)

class bikes ():

    # constructor
    def __init__(self):
        self.pmileage=int(input("enter the pmilage "))
        self.pcapacity=int(input("enter the pcapacity "))
        self.hmileage=int(input("enter the hmileage "))
        self.hcapacity=int(input("enter the hcapacity "))

    def comp (self):
        if(self.pmileage < self.hmileage):
            print("{} pmileage is more efficent".format(self.pmileage))
        else:
            print("{} hmileage is more efficent".format(self.hmileage))


yy= bikes()
yy.comp()



class bikes2 ():
    def __init__(self,pmileage,hmileage):
        self.pmileage=pmileage
        self.hmileage=hmileage
    def comp (self):
        if(self.pmileage > self.hmileage):
            print("{} pmileage is more efficent".format(self.pmileage))
        else:
            print("{} hmileage is more efficent".format(self.hmileage))
yy= bikes2(2,5)
yy.comp()
















