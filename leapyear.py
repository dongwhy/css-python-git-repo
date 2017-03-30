#4로 나뉘어 떨어지면 윤년
#100으로 나뉘어 떨어지면 평년,
#400으로 나뉘어 떨어질땐 윤년

def check_year(year):
	if year % 400 == 0 :
		print("leap_year")
	elif year % 4 == 0 and year % 100 != 0 :
		print("leap_year")
	else:
		print("normal year")

year = int( input("input year : "))
check_year(year)
