#!/usr/bin/python

import random

def konflikt((r1, c1), (r2, c2)):
	if(r1 == r2):									return True
	if(c1 == c2):									return True
	if(r1 / 3 == r2 / 3 and c1 / 3 == c2 / 3 and (not (r1 == r2 and c1 == c2))):	return True
	return False

def setminus(lst1, lst2):
	return [x for x in lst1 if x not in lst2]

def sled_celija((i, j)):
	if(j == 8):
		if(i == 8):	return (0, 0)
		return (i + 1, 0)
	return (i, j + 1)

def rjesenje(input):
	empty = [[0] * 9] * 9
	def uslov(pos, sudoku):
		def dozvoljene_vrijednosti():
			konflikti = set([ (r, c) for r in range(9) for c in range(9) if((r, c) != pos and konflikt(pos, (r, c)))])
			nedozvoljeni = set([sudoku[r][c] for (r, c) in konflikti if sudoku[r][c] != 0])
			s = setminus(range(1, 10), nedozvoljeni)
			random.shuffle(s)
			return s
		if(sudoku[pos[0]][pos[1]] != 0):
			if(pos != (8, 8)):	return uslov(sled_celija(pos), sudoku)
			else:			return sudoku

		values = dozvoljene_vrijednosti()
		if(values == empty): return empty
		new = [r[:] for r in sudoku]
		for value in values:
			new[pos[0]][pos[1]] = value
			filled = uslov(sled_celija(pos), new)
			if(filled != empty):	return filled
		return empty
	return uslov((0, 0), input)

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

def napravi_problem(sudoku):
	def nasumicna_lista(num, lst):
		index = random.randint(0, len(lst) - 1)
		result = [lst.pop(index)]
		if(num > 1):
			result.extend(nasumicna_lista(num - 1, lst))
		return result

	for rowNum in range(9):
		row = sudoku[rowNum]
		offset = random.randint(0, 1)
		napravi_problemIndices = nasumicna_lista(5 + offset, range(9))
		for i in napravi_problemIndices:
			row[i] = '_'
	return sudoku

if __name__ == '__main__':
	sudoku = [[0] * 9] * 9
	print 'nedozvoljeni:'
	solution = rjesenje(sudoku)
	printSudoku(solution)
	print 'problem:'
	printSudoku(napravi_problem(solution))
