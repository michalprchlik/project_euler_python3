# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def find_triplet(max_number):
	array = []
	for i in range(1, max_number):
		for j in range(i + 1 , max_number):
			for k in range(j + 1, max_number):
				is_valid = is_triplet_valid(i, j, k, max_number)
				if is_valid:
					array = [i, j, k]
	return array

def get_product(array):
	product = array[0] * array[1] * array[2]
	return product

def is_triplet_valid(i, j, k, max_number):
	sum_number = i + j + k
	is_valid = True
	if i == j or i == k or j == k:
		is_valid = False
	elif i > j or i > k:
		is_valid = False
	elif j < i or j > k:
		is_valid = False
	elif sum_number != max_number:
		is_valid = False
	else:
		square_ij = i ** 2 + j ** 2
		square_k = k ** 2
		if square_ij != square_k:
			is_valid = False

	return is_valid
