# 2로 나누고 곱하는 과정으로 두 수의 곱을 구현하는 방법

'''
# 모듈화하기

# 몫 홀/짝 체크
def checkNum(num):
	if (num // 2) % 2 == 0:
		return "even"
	else :
		return "odd"

# main
def main(a_val, b_val):
	while a_val > 0 :
		if checkNum(a_val) == "even":
			a_value = a_value // 2
			b_value *= 2
			print("struck --")
		else :
			a_value = a_value // 2
			b_value *= 2
			keep_list.append(b_value)
'''


keep_list = []

a_value = 0
b_value = 0

numberlist = str(input("input two number with SPACE : ")).split()

a_value = int(numberlist[0])
b_value = int(numberlist[1])

while a_value // 2 > 0:
	if (a_value // 2) % 2 == 0: # 몫이 짝수일때 struck
		a_value = a_value // 2
		b_value *= 2
		print("%4d %7d struck ---" %(a_value, b_value))
	else : # 몫이 홀수일때 keep
		a_value = a_value // 2
		b_value *= 2

		keep_list.append(b_value)

		print("%4d %7d keep %d" %(a_value, b_value, b_value))

print("==>",end='')

sum = 0
for i in keep_list:
	sum += i
	print("%d "%(i) ,end='')
	
print("= %d " %(sum))
