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


		







print(test_palindrome("hannah"))
print(test_palindrome("car"))
print(test_palindrome('abcd'))
print(test_palindrome('abacaba'))

# with open("in.txt") as f:
# 	for line in f:
# 		print(line)