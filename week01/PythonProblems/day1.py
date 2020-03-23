def sum_of_digits(n):
	total = 0

	if n < 0:
		n *= -1

	while n > 0:
		total += n%10
		n = n // 10

	return total


def to_digits(n):
	return [int(i) for i in str(n)]


def to_number(digits):
	evr = ''
	for i in digits:
		evr += str(i)
	return int(evr)


def fact_digits(n):
	sums = 0
	string_input = str(n)
	for num in string_input:
		factorial = 1
		for i in range(1,int(num)+1):
			factorial *= i
		sums += factorial
	return sums


def palindrome(n):
	string_input = str(n)
	for i in range(0,len(string_input)//2):
		if string_input[i] !=  string_input[len(string_input)-i-1]:
			return False
	return True


def count_voweles(string):
	low_string = string.lower()
	sums = 0
	voweles = ['a','i','u','y','e','o']
	for char in low_string:
		for vow in voweles:
			if vow == char:
				sums += 1
	return sums


def count_consonants(string):
	low_string = string.lower()
	sums = 0
	for char in low_string:
			if char != 'a' and char != 'i' and char != 'u' and char != 'y' and char != 'e' and char != 'o' and ord(char) >= 97 and ord(char) <= 122:
				sums += 1
	return sums


def char_histogram(string):
	histogram = {}
	for char in string:
		count = string.count(char)
		histogram.update({char : count})
	return histogram


def sum_matrix(m):
	sums = 0
	for sub_mat in m:
		for num in sub_mat:
			sums+= num
	return sums


def nan_expand(times):
	part1 = "Not a "
	part2 = "NaN"
	starting = ""
	if times != 0:
		for i in range(times):
			starting += part1
		starting += part2
	return starting


def prime_factors(n):
	factors = []
	if n > 1:
		i = 2
		while n % i != 0:
			i += 1
		factors.append(i)
		factors.extend(prime_factors(n / i))
	return factors


def prime_factorization(n):
	list1 = []
	vals = prime_factors(n)
	for i in vals:
		numb = vals.count(i)
		list1.append((i,numb))
		for s in range(numb-1):
			vals.remove(i)
	return list1


def group(n):
	ls = []
	for val in n:
		if not ls:
			ls.append([val])
			k = 0
			continue
		if val == ls[k][0]:
			ls[k].append(val)
		else:
			k += 1
			ls.append([val])
	return ls


def max_consecutive(items):
	vals = group(items)
	max_c = 0
	for i in range(len(vals)):
		if max_c < len(vals[i]):
			max_c = len(vals[i])
	return max_c


def main():
	print(sum_of_digits(0))
	print(to_digits(123023))
	print(to_number([3,5,7,1]))
	print(fact_digits(999))
	print(palindrome('kappak'))
	print(count_voweles("A nice day to code!"))
	print(count_consonants("A nice day to code!"))
	print(char_histogram("Python!"))
	# m = [[1,2,3],[4,5,6],[7,8,9]]
	m = [[1,2],[3,4],[5,6],[7,8],[9,10]]
	print(sum_matrix(m))
	nan_expand(4)
	print(prime_factorization(356))
	print(group([1,1,1,2,3,1,1]))
	print(max_consecutive([1,1,2,2,3,3,4,4,5,5,5]))

main()
