# Ransome note Problem states that -> there are two strings ransomeNote and Magzine 
# You have to find that , all character from ransomeNote string could be formed from  the charcter present in the Magzine or not 
# Note :- Each Character of Magzine should be calculated only once in the RansomeNote


#Approach 
#step 1 : define an empty dictionary 
#step 2 : iterate over Magzine(Always Second String) and store character as key and  frequency as value of that character in the Dictionary
#step 3 : now iterate over next string RansomeNote , and check weather character is found in the dictionary or not 
	# substep 3 : if found reduce character frequency from the Dictionary by one 
	# substep 3 : if not found  , simply return False
#step 4 : return True 




def ransome_note(rans , mag):
	tem_dict = {}
	for char in mag:
		print("current Character in mag :", char)
		tem_dict[char] = tem_dict.get(char , 0) +1
	print("My dict looks like this : " , tem_dict)
	
	for char in rans:
		if char not in tem_dict or tem_dict.get(char) == 0:
			return False
		tem_dict[char] = tem_dict.get(char)-1
		
	return True

if __name__ == "__main__":
	rans = str(input("Enter your Ransome String : "))
	mag = str(input("Enter your Magzine String : "))
	result = ransome_note(rans , mag)
	if result :
		print("True")
	else:
		print("False")
	
		
