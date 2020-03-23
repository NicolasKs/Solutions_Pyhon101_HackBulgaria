import sys
from random import randint


def generate_numbers(filename, numbers):
	with open(filename,'w') as f:
		for i in range(numbers):
			f.write(str(randint(1,1000)))
			if i + 1 < numbers:
				f.write(' ')


def main():
	generate_numbers(sys.argv[1],int(sys.argv[2]))


if __name__ == '__main__':
	main()