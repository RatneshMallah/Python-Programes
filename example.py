def max_num(my_list):
	x = 0
	i = 0
	y = 1
	for item in my_list:
		if a[x]>a[y]:
			x -= 1
			y += 1
			print(x)
		elif a[x]<a[y]:
			x += 1
			y -= 1
			print(y)
