import random # module 模組

start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)

r =  random.randint(start, end) # 包括 1 and 100

count = 0

while True:
	count += 1 # count = count + 1
	a = input('請猜數字: ')
	a = int(a)

	if a == r:
		print('恭喜你答對了!')
		print('你猜了第', count, '次')
		break

	elif a > r:
		print('比答案大!')
		
	else:
		print('比答案小!')

	print('你猜了第', count, '次')