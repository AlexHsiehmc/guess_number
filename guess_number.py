import random # module 模組

r =  random.randint(1, 100) # 包括 1 and 100

while True:
	a = input('請猜數字: ')
	a = int(a)

	if a == r:
		print('恭喜你答對了!')
		break

	elif a > r:
		print('比答案大!')

	else:
		print('比答案小!')