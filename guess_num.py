import random

r = random.randint(1, 50)
count = 0
while True:
	count += 1
	print('')
	print('這是你猜的第', count, '次')

	num = input('輸入數字: ')
	num = int(num)

	if num == r:
		print("你猜中了!")
		break
	elif num < r:
		print("比數字小")
	elif num > r:
		print("比數字大")

