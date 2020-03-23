def gas_stations(distance,tank_size,stations):
	stations.append(distance)
	ls = []
	counter = 0
	for i in range(len(stations)):
		if not ls:
			if abs(stations[i] - tank_size) <= abs(stations[i+1] - tank_size):
				ls.append(stations[i])
				continue
		else:
			if abs(ls[counter] - stations[i]) > tank_size:
				if stations[i] - tank_size > 0:
					ls.append(stations[i-1])
					counter += 1
	return ls

def is_number_balanced(number):
	digits = str(number)
	if len(digits) % 2 != 0:
		left = digits[0:len(digits)//2]
		right = digits[len(digits)//2 +1 :]
	else:
		left = digits[:len(digits)//2]
		right = digits[len(digits)//2:]

	if sum([int(i) for i in left]) == sum([int(i) for i in right]):
		return True
	return False


def increasing_or_decreasing(seq):
	posit = all(i < j for i, j in zip(seq,seq[1:]))
	neg = all(i > j for i, j in zip(seq,seq[1:]))

	if posit > neg:
		return "Up !"
	elif neg > posit:
		return "Down !"
	return False

def sum_of_numbers(number):
	nums = ''
	sum_tot = 0
	for vals in number:
		try:
			int(vals)
		except:
			nums += ','
		else:
			nums += vals
	list_nums = nums.split(',')
	for vals in list_nums:
		if not vals:
			pass
		else :
			sum_tot += int(vals)
	return sum_tot


def birthday_ranges(birthdays,ranges):
	rangez = [range(i[0],i[1] + 1) for i in ranges]
	birthdays_per_range = []

	for dates in rangez:
		birthday_count = 0
		for day in birthdays:
			if day in dates:
				birthday_count += 1
		birthdays_per_range.append(birthday_count)
		
	return birthdays_per_range


def main():
	# print(gas_stations(320,90,[50,80,140,180,220,290]))
	print(gas_stations(390,80,[70,90,140,210,240,280,350]))
	print(is_number_balanced(1238033))
	print(increasing_or_decreasing([1,2,3,4,5,6]))
	print(sum_of_numbers("abc125de4"))
	# print(sum_of_numbers("0abcasfdsgd"))
	print(birthday_ranges([1,2,3,4,5],[(1,2),(1,3),(1,4),(1,5),(4,6)]))
	
main()