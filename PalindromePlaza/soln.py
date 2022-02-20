# solution

def test_palindrome(in_str):
	"""
	Tests if a str can be made into a palindrome
	if so, ret 1, else, 0

	Rules:
	If str length even, need all even amount of chars
	Else, can have one odd char and rest must be even
	"""
	char_dict = {}

	# loop thru each char, check count
	for char in in_str:
		# if in, increment count
		if char in char_dict:
			char_dict[char] +=1
		# else, create entry
		else:
			char_dict[char] = 1

	# even case
	# need all entries even
	if len(in_str) %2 == 0:
		for k in char_dict:
			if char_dict[k] % 2 != 0:
				return 0

		return 1
	
	# odd case
	# need all entries even except for one
	# or if length is 1, that is defined as palindrome
	else:
		one_char_count = False
		for k in char_dict:
			# odd count
			if char_dict[k] % 2 != 0:
				# this is the one shot!
				if(one_char_count):
					return 0
				else:
					one_char_count = True	
		
		return 1

# function to test each row, column, and diagonal
def test_mat(mat):
	# square mat
	cols = len(mat[0])
	# counter for palindromes
	pal_count = 0
	# first we do rows
	for n,i in enumerate(mat):
		pal_count += test_palindrome(i)
	# test columns
	for i in range(cols):
		col = "".join([sub[i] for sub in mat])
		pal_count += test_palindrome(col)
	
	# first go top left to bottom right
	for i in range(0,cols):
		curr_row = 0
		curr_col = i
		curr_str = ""
		for j in range(i +1):
			curr_str += mat[curr_row][curr_col]
			curr_row +=1
			curr_col -=1
		pal_count += test_palindrome(curr_str)
	# # go the other way
	for i in range(0,cols-1):
		curr_row = cols - 1
		curr_col = cols - i -1
		curr_str = ""
		for j in range(i+1):
			curr_str += mat[curr_row][curr_col]
			curr_row -=1
			curr_col +=1
		pal_count += test_palindrome(curr_str)
	
	# now go top right to bottom left
	# first half
	for i in range(0,cols):
		curr_row = 0
		curr_col = cols-i-1
		curr_str = ""
		for j in range(i+1):
			curr_str += mat[curr_row][curr_col]
			curr_row +=1
			curr_col +=1
		pal_count += test_palindrome(curr_str)
	# next half
	for i in range(0,cols-1):
		curr_row = cols - 1
		curr_col = i
		curr_str = ""
		for j in range(i+1):
			curr_str += mat[curr_row][curr_col]
			curr_row -=1
			curr_col -=1
		pal_count += test_palindrome(curr_str)
	
	return pal_count

def solve_from_file(file_name):
	# read file, solve problem
	with open(file_name,"r") as f:
		lines = f.readlines()
		mat = []
		for line in lines:
			# be sure to remove new lines!
			mat.append(line.replace("\n",""))
		return test_mat(mat)

# gen cases
import string
import random

def gen_cases(case_count,base_dir):
	# base dir == samples
	# always square matrix
		for i in range(case_count):
			# get random word size each time
			word_size = random.randint(3,50)
			file_name = base_dir + "/inputs/input{}{}.txt".format(i//10,i%10)
			with open(file_name,"w") as f:
				for j in range(word_size):
					curr_word = ''.join(random.choices(string.ascii_lowercase,k=word_size))
					print(curr_word,file=f)

import os
import re
def gen_solns(base_dir):
	# base dir == samples
	# read the files
	for f in os.listdir(base_dir + "/inputs"):
		file_name = os.path.join(base_dir+"/inputs",f)
		# read file
		soln = solve_from_file(file_name)
		# write to file
		number_of_file = re.findall(r'\d+',file_name)[0]
		output_name = base_dir + "/outputs/output{}.txt".format(number_of_file)
		with open(output_name,"w") as f:
			print(soln,file=f)

## gen cases and then solns
# gen_cases(100,"./samples")
# gen_solns("./samples")




		

# mat0 = [
# 	'abcd',
# 	'efgh',
# 	'ijkl',
# 	'mnop',
# ]
# mat1 = [
# 	'aba',
# 	'dcd',
# 	'aba'
# ]
# mat2 = [
# 	'abba',
# 	'bacd',
# 	'badc',
# 	'abdd'
# ]
# print(test_mat(mat2))