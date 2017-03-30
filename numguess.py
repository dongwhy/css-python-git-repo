import random

answer = random.randint(1,100)
print(answer)

username = input("What is your name? ")
chance = 3

while 1:
	guess = eval(input("hi, " + username + ", GUess the number: "))
	chance -= 1
	
	if chance == 0 :
		print("You are dead. ")
		break
	elif guess == answer:
		print("Correct!")
		break
	elif guess > answer :
		print(str(guess) + " > answer, chance : " + str(chance))
	elif guess < answer :
		print(str(guess) + " < answer, chance : " + str(chance))

	
	
	
