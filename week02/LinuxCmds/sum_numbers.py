import sys



def sum_numbers(filename):
	with open(filename, 'r') as f:
		data = f.readline()

	data = data.split(' ')
	sums = 0
	for i in data:
		sums += int(i)

	print(sums)



def main():
	sum_numbers(sys.argv[1])



if __name__ == '__main__':
	main()