#• Check if two strings are anagrams.
#step1 : check if length of string1 and length of string2 is same or not , if not same return false 
#step2 : initialize an empty dictionary 
#step3 : iterate over string1 and store current character as key and value as it count
#step4 : iterate over second string "String2" , check if character is in the map(dictionary) or not and its value is > 0 or not ,if this condition satisfy , decrease its count by 1 , else return False


def anagram(string1 , string2):
	if len(string1) !=len(string2):
		return False
	frequency_check = {}
	for char in string1:
		#print(char,"current char in string1")
		frequency_check[char] = frequency_check.get(char , 0)+1
	print(frequency_check)
	
	for char in string2:
		if frequency_check.get(char , 0) > 0:
			#frequency_check[char] =frequency_check.get(char)-  1
			frequency_check[char] -=1
		else:
			False
	return True 
	
	
	
		
	
	

if __name__ == "__main__":
	string1 = str(input("Enter the First String : "))
	string2 = str(input("Enter the Second String : "))
	re = anagram(string1 , string2)
	if re == True :
		print("Given two string are Anagram :")
	else:
		print("Given two string are not Anagram :")
	
