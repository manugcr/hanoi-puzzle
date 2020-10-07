## Hanoi puzzle solver with recursion.
##
## call hanoi(num, tower1, tower2, tower3) function with the number  
## of disks you have and the names of each tower.
##
##    |        |        |
##	  |		   |	    |
##	  |		   |	    |
## -------  -------  -------
##	  A        B        C

def move(start_pos, target_pos):
	global count
	print(f'Move disc from {start_pos} to {target_pos}')
	count += 1

def hanoi(num_disks, start_pos, helper, target_pos):
	if num_disks == 0:
		pass
	else:
		hanoi(num_disks - 1, start_pos, target_pos, helper)
		move(start_pos, target_pos)
		hanoi(num_disks - 1, helper, start_pos, target_pos)
		

count = 0
n = int(input('How many disks you have? '))
hanoi(n, 'A', 'B', 'C')
print(f'\nYou need {count} steps.')