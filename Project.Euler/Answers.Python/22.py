# problem 22
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 17, 2015'

def letterScore(letter):
	score = 0
	if letter == 'A' or letter == 'a':
		score = 1
	elif letter == 'B' or letter == 'b':
		score = 2
	elif letter == 'C' or letter == 'c':
		score = 3
	elif letter == 'D' or letter == 'd':
		score = 4
	elif letter == 'E' or letter == 'e':
		score = 5
	elif letter == 'F' or letter == 'f':
		score = 6
	elif letter == 'G' or letter == 'g':
		score = 7
	elif letter == 'H' or letter == 'h':
		score = 8
	elif letter == 'I' or letter == 'i':
		score = 9
	elif letter == 'J' or letter == 'j':
		score = 10
	elif letter == 'K' or letter == 'k':
		score = 11
	elif letter == 'L' or letter == 'l':
		score = 12
	elif letter == 'M' or letter == 'm':
		score = 13
	elif letter == 'N' or letter == 'n':
		score = 14
	elif letter == 'O' or letter == 'o':
		score = 15
	elif letter == 'P' or letter == 'p':
		score = 16
	elif letter == 'Q' or letter == 'q':
		score = 17
	elif letter == 'R' or letter == 'r':
		score = 18
	elif letter == 'S' or letter == 's':
		score = 19
	elif letter == 'T' or letter == 't':
		score = 20
	elif letter == 'U' or letter == 'u':
		score = 21
	elif letter == 'V' or letter == 'v':
		score = 22
	elif letter == 'W' or letter == 'w':
		score = 23
	elif letter == 'X' or letter == 'x':
		score = 24
	elif letter == 'Y' or letter == 'y':
		score = 25
	elif letter == 'Z' or letter == 'z':
		score = 26
	return score

def nameScore(name):
	score = 0
	for s in name:
		score += letterScore(s)
	return score

def totalScore(names):
	totalscore = 0
	for i, e in enumerate(names):
		print(i+1, e)
		totalscore += (i+1) * nameScore(e)
	return totalscore

def solution():
	filename = 'p022_names.txt'
	f = open(filename, 'r', encoding = 'utf-8')
	names = f.read()[1:-1]
	names = names.split('","')
	names = sorted(names)
	print(names)
	totalscore = totalScore(names)
	print(totalscore)

solution()
