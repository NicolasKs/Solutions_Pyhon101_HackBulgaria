def if_anagrams():
	word1 = input('Enter word1: ')
	word2 = input('Enter word2: ')

	if len(word1) != len(word2):
		return 'Not Anagrams'
	else:
		symbols = [i.lower() for i in word2]
		checker = [i.lower() for i in word1]

	for sym in symbols:
		try:
			checker.remove(sym)
		except:
			return 'Not Anagrams'

	return 'Anagrams'


def to_number(digits):
	evr = ''
	for i in digits:
		evr += str(i)
	return evr


def is_credit_card_valid(number):
	digits = [i for i in str(number)]
	sum_tot = 0
	if len(digits) % 2 != 0:
		for i in range(len(digits)):
			if i % 2 != 0:
				digits[i] = int(digits[i])*2
		back_str = to_number(digits)
		for i in back_str:
			sum_tot += int(i)
		if sum_tot % 10 != 0:
			return '{} , is invalid number'.format(number)
	else:
		return '{} , is invalid number'.format(number) 
	return "{}, is a valid number".format(number)

	
def give_primes(num):
	primes = []
	for Numbers in range(2,num+1):
		if Numbers > 1:
			for i in range(2,Numbers):
				if Numbers % i == 0:
					break
			else:
				primes.append(Numbers)
	return primes


def goldbach(number):
	primes = give_primes(number)
	ls=[]
	for i in primes:
		for s in primes:
			if i + s == number:
				ls.append((i,s))
				primes.remove(s)
	return ls


def main():
	print(if_anagrams())
	print(is_credit_card_valid(79927398715)) #79927398713
	print(goldbach(100)) # 4 , 6 , 8 , 10
	
main()