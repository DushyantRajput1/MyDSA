#Longest Sub string without repeating character

def lsswrc(string):
	dict = {}
	left = 0 
	right = 0
	max_length = 0
	while right < len(string):
		if string[right] in dict:
			left = max(left,dict[string[right]]+1)
		dict[string[right]] = right 
		max_length = max(max_length , (right-left+1))
		right +=1
	return max_length
	
if __name__ == "__main__":
	string = str(input("Enter your string : "))
	result = lsswrc(string)
	print("Resultant Non repeting character length is : " , result)
	
