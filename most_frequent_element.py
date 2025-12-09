#most frequent element in the array

from anagram import count_frequency
def most_frequency_count(string):
	max_count = 0
	max_count_fr = ""
	result = count_frequency(string)
	for char in result:
		if result.get(char) > max_count:
			max_count = result.get(char)
			max_count_fr = char
			
	return max_count_fr
		





if __name__ == '__main__':
	string = str(input("Enter Your String: "))
	result = most_frequency_count(string)
	print("Maximum count of element is " , result)
	
	
