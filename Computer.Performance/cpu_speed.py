'''
cpu_speed.py
'''

import time

__author__ = 'Libao Jin'
__date__ = 'July 21, 2015'

def rocknroll(upper_bound):
	number = 1
	while number < upper_bound:
		number += 1

if __name__ == '__main__':
	times = range(10)
	all_time = 0
	upper_bound = 100000000
	for i in times:
		start_time = time.time()
		rocknroll(upper_bound)
		end_time = time.time()
		interval = end_time - start_time
		all_time += interval
		print('Elapsed time: {0:.2f}'.format(interval))
	print('All elapsed time: {0:.2f}'.format(all_time))
