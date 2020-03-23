# cat2.py
import sys


def cat2(args):
	for i in range(len(args)):
		if args[i] == 'cat2.py':
			continue
		with open (args[i], 'r') as f:
			data = f.read()
			print(data)
			try:
				args[i+1]
			except:
				continue
			else:
				print()


def main():
	cat2(sys.argv)



if __name__ == '__main__':
	main()