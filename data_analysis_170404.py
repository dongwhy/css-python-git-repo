
# coding: utf-8

# In[13]:

# 절차지향으로 구현
# score = [95, 23, 46, 25]
# scores [95, 23, 25, 62] avrg : 50
#  sum((각 점수 - 평균)**2 )/ 데이터의 개수
from functools import reduce

def average(score):
    return reduce(lambda a, b : a + b, score)/ len(score)

def variance(score, avrg):
    return reduce(lambda a, b : a + b , map(lambda e : (e - avrg)**2, score))/len(score)

def evaluateClass(avrg, std_dev):
    if avrg <50 and std_dev >20:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avrg > 50 and std_dev >20:
        print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
    elif avrg < 50 and std_dev <20:
        print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
    elif avrg > 50 and std_dev <20:
        print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")


# In[2]:

f = open("class_A.bin", "rb")


# In[34]:

items = []

import pickle

while True :
    try :
        data = pickle.load(f)
    except EOFError:
        break
    items.append(data)

f.close()


# In[5]:

print(items)


# In[6]:

# li = [95, 25, 50, 15 ,... ,20]
scores = []

def items_value(items):
    for i in items :
        for value in i.values() :
            scores.append(value)
            


# In[8]:

items_value(items)


# In[9]:

scores


# In[10]:

dic = dict(one = 1, two = 2, three = 3)


# In[11]:

for key, value in dic.items():
    pass
for one in dic.items():
    print(one)


# In[14]:

avrg = average(scores)


# In[15]:

avrg


# In[16]:

vari = round(variance(scores, avrg), 1)


# In[17]:

vari


# In[21]:

import math
std_dev = round(math.sqrt(vari), 1)


# In[22]:

std_dev


# In[33]:

print("\n")

print('*' * 50)
print("A반 성적 분석 결과")
print('*' * 50)
print("A반의 평균은 {0}점이고 분산은 {1}이며, 따라서 표준편차는 {2}이다".format(avrg, vari, std_dev))
print('*' * 50)
print("A반 종합 평가")
print('*' * 50)

print('\n')


# In[ ]:



