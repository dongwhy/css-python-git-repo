
# coding: utf-8

# In[8]:

class Stack(list): 
    push = list.append 


    def is_empty(self): 
        if not self: 
            return True 
        else: 
            return False 


    def peek(self): 
        return self[-1] 


# In[9]:
if __name__ == "__main__" :
    s = Stack() 
    s.push(1) 
    s.push(2) 
    s.push(3) 
    s.push(4) 
    s.push(5) 

    while not s.is_empty():
        data = s.pop() 
        print(data, end = '  ') 


# In[ ]:



