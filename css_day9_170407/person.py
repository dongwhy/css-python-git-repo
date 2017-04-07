
# coding: utf-8

# In[1]:

class Person : 
    def __init__(self, name, age, money) :
        self.name = name
        self.age = age
        self.money = money
        
    def give_money(self, other, how_much) :
        self.money -= how_much
        other.money += how_much
        
    def __str__(self) :
        return '''
My name is {} 
I am {} years old
I have {} won'''.format(self.name, self.age, self.money)

if __name__ == "__main__" :
    # In[2]:

    p1 = Person("greg", 18, 5000)


    # In[3]:

    p2 = Person("kim", 22, 1000)


    # In[4]:

    print(p1)


    # In[5]:

    print(p2)


    # In[6]:

    p1.give_money(p2, 2000)


    # In[7]:

    print(p1)


    # In[8]:

    print(p2)


# In[ ]:

# Person 을 상속받는 Buyer 라는 클래스를 만들기

