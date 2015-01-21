#!/usr/bin/python

import random

def conflict((r1, c1), (r2, c2)):
	if(r1 == r2):									return True
	if(c1 == c2):									return True
	if(r1 / 3 == r2 / 3 and c1 / 3 == c2 / 3 and (not (r1 == r2 and c1 == c2))):	return True
	return False

def setminus(lst1, lst2):
	return [x for x in lst1 if x not in lst2]

def nextcell((i, j)):
	if(j == 8):
		if(i == 8):	return (0, 0)
		return (i + 1, 0)
	return (i, j + 1)

def solve(input):
	empty = [[0] * 9] * 9
	def satisfy(pos, sudoku):
		def getAllowedValues():
			conflicts = set([ (r, c) for r in range(9) for c in range(9) if((r, c) != pos and conflict(pos, (r, c)))])
			notallowed = set([sudoku[r][c] for (r, c) in conflicts if sudoku[r][c] != 0])
			s = setminus(range(1, 10), notallowed)
			random.shuffle(s)
			return s
		if(sudoku[pos[0]][pos[1]] != 0):
			if(pos != (8, 8)):	return satisfy(nextcell(pos), sudoku)
			else:			return sudoku

		values = getAllowedValues()
		if(values == empty): return empty
		new = [r[:] for r in sudoku]
		for value in values:
			new[pos[0]][pos[1]] = value
			filled = satisfy(nextcell(pos), new)
			if(filled != empty):	return filled
		return empty
	return satisfy((0, 0), input)

def printSudoku(sudoku):
	print '-------------------------'
	for i in range(9):
		for j in range(9):
			if(j == 8):	print sudoku[i][j]
			elif(j%3 == 2):	print str(sudoku[i][j]) + '|',
			else:		print str(sudoku[i][j]) + ' ',
		if(i%3 == 2):
			print '-------------------------'
	print

def mask(sudoku):
	def generateRandomList(num, lst):
		index = random.randint(0, len(lst) - 1)
		result = [lst.pop(index)]
		if(num > 1):
			result.extend(generateRandomList(num - 1, lst))
		return result

	for rowNum in range(9):
		row = sudoku[rowNum]
		offset = random.randint(0, 1)
		maskIndices = generateRandomList(5 + offset, range(9))
		for i in maskIndices:
			row[i] = '_'
	return sudoku

if __name__ == '__main__':
	sudoku = [[0] * 9] * 9
	print 'solution:'
	solution = solve(sudoku)
	printSudoku(solution)
	print 'masked:'
	printSudoku(mask(solution))
