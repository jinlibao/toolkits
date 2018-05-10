'''
ppi.py
Compute pixels per inch.
'''

import math

__author__ = 'Libao Jin'
__date__ = 'July 21, 2015'

class Screen():
	'''
	Class: A Digital Screen 
	'''

	def __init__(self):
		'Constructor'
		self.ppi = None

	def __init__(self, **screen_info):
		'Constructor'
		self.width = screen_info['width']
		self.height = screen_info['height']
		self.size = screen_info['size']

	def compute_ppi(self, width, height, size):
		ppi = math.sqrt(width ** 2 + height ** 2) / size
		print('-' * 40)
		print('Screen size: {0:.1f} inches'.format(size))
		print('Resolution')
		print('width: {0:d}'.format(width))
		print('height: {0:d}'.format(height))
		print('ppi: {0:.1f}'.format(ppi))

	def set_ppi(self):
		self.ppi = math.sqrt(self.width ** 2 + self.height ** 2) / self.size

	def get_width(self):
		'Get width.'
		return self.width

	def get_height(self):
		'Get height.'
		return self.height

	def get_size(self):
		'Get size.'
		return self.size

	def get_ppi(self):
		'Get ppi.'
		return self.ppi

	def get_screen_info(self):
		'Get screen detailed info.'
		print('-' * 40)
		print('Screen size: {0:.1f} inches'.format(self.size))
		print('Resolution')
		print('width: {0:d}'.format(self.width))
		print('height: {0:d}'.format(self.height))
		print('ppi: {0:.1f}'.format(self.ppi))


if __name__ == '__main__':
	width = 1280
	height = 720
	size = 5.5
	screen_info = {'width': width, 'height': height, 'size': size}
	s = Screen(**screen_info)
	s.set_ppi()
	s.get_screen_info()
	s.compute_ppi(1920, 1080, 5.7)
	s.compute_ppi(2560, 1440, 5.7)
	s.compute_ppi(1366, 768, 13.6)
	s.compute_ppi(1920, 1080, 5.5)
	s.compute_ppi(1280, 768, 5)
	s.compute_ppi(1920, 1080, 4.95)
	s.compute_ppi(1136, 640, 4)
	s.compute_ppi(2560, 1600, 13.3)
	s.compute_ppi(2880, 1800, 15.4)
