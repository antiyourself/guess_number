import random

r = random.randint(1, 50)

while True:
	num = input('輸入數字: ')
	num = int(num)

	if num == r:
		print("你猜中了!")
		break
	elif num < r:
		print("比數字小")
	elif num > r:
		print("比數字大")

