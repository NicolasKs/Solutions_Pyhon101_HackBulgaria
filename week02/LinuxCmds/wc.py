import sys


def counter(search_type,filename):
	with open(filename,'r') as f:
		lines = 0
		words = 0
		chars = 0
		for line in f:
			wordslist = line.split()
			lines += 1
			words += len(wordslist)
			chars += len(line)
		if search_type == 'lines':
			print(lines)
		elif search_type == 'words':
			print(words)
		elif search_type == 'chars':
			print(chars)


def main():
	counter(sys.argv[1],sys.argv[2])




if __name__ == '__main__':
	main()