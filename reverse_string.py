#• Reverse a string without using built-in reverse functions.
#initialize a empty string 
#iterate character from the string from last character to starting of the string
#add current string into the empty string

def reverse_string(string):
	result = ""
	size = len(string)
	indx = size-1
	while indx>-1:
		print("current char is :" , string[indx])
		result = result + string[indx]
		indx -= 1
	return result

if __name__ == '__main__':
	letters = str(input("Enter the string to be reversed :"))
	re = reverse_string(letters)
	print("Resultant String is :" ,re)
	

