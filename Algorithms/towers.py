def move(number, source, destination):
	if (number == 1):
		print("Move from:", source, " to:", destination)
		return
	
	#move from source to tmp number-1 of rings
	tmp = 6 - source - destination
	move(number - 1, source, tmp);
	print("Move from:", source, " to:", destination)
	move(number - 1, tmp, destination)

move(10, 1, 3)
#Move piramid N-1 from 1 to tmp = 6-3-1 = 2
#Move piramid 1 from 1 to 3
#Move piramid N-2 form tmp to new_tmp
