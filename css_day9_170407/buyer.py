from person import Person
from retailer import Retailer

class Buyer(Person):
    def __init__(self, name, age, money, product):
        super().__init__(name, age, money)
        self.product = product
    
    def buy(self, other, how_many):
        other.sell(self, how_many)
        self.product += how_many
        
    def __str__(self):
        return super().__str__() + '''
I am a buyer.
I have {} products'''.format(self.product)
    
if __name__ =="__main__" :
    b1 = Buyer("greg", 18, 3000, 0)
    r1 = Retailer("kim", 25, 2000, 20)

    print(b1)
    print(r1)

    b1.buy(r1, 3) # 3개를 구매하기
    
    print(b1)
    print(r1)