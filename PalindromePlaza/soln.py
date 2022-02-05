# solution

data = None

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
	
	# test diagonals (only one direction)
	for i in range(0,cols):
		curr_row = 0
		curr_col = i
		curr_str = ""
		for j in range(i +1):
			curr_str += mat[curr_row][curr_col]
			curr_row +=1
			curr_col -=1
		pal_count += test_palindrome(curr_str)
	# go the other way
	for i in range(0,cols-1):
		curr_row = cols - 1
		curr_col = cols - i -1
		curr_str = ""
		for j in range(i+1):
			curr_str += mat[curr_row][curr_col]
			curr_row -=1
			curr_col +=1

		pal_count += test_palindrome(curr_str)
	
	return pal_count


		

mat0 = [
	'abcd',
	'efgh',
	'ijkl',
	'mnop',
]
mat1 = [
	'aba',
	'dcd',
	'aba'
]
print(test_mat(mat1))





# with open("in.txt") as f:
# 	for line in f:
# 		print(line)