import random

answer = random.randint(1,100)
print(answer)

username = input("What is your name? ")
while 1:
	guess = eval(input("hi, " + username + ", GUess the number: "))

	if guess == answer:
		print("Correct!")
		break
	elif guess > answer :
		print(str(guess) + " > answer")
	elif guess < answer :
		print(str(guess) + " < answer")
	else :
		print("You are wrong!")

	
	
	
