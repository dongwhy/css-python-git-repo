from person import Person

class Retailer(Person) :
    price = 1000 # product의 가격
    
    #생성자
    def __init__(self, name, age, money, product):
        super().__init__(name, age, money)
        self.product = product
    
    def sell(self, other, how_many ):
        if self.product > how_many:
            self.product -= how_many
            total = self.price * how_many
            other.give_money(self, total)
        
        else :
            print("물량부족")
    
    def __str__(self):
        return super().__str__() + '''
I am a retialer.
I have {} products
        '''.format(self.product)
    
if __name__ == "__main__" :
    r1 = Retailer("yang", 20, 5000, 20)
    p1 = Person("kim", 13, 10000)
    print(r1)
    print(p1)
    r1.sell(p1, 3)
    print(r1)
    print(p1)