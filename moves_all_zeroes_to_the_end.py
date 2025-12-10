# Moves all Zeroes at the end of the array 

#==================Approach 1=======================
#step 1:- create temporary empty array and count .
#step 2:- traverse over the origial array , if non zero array found copy it into the temporary array and increment the count
#step 3:- second traversal start from count till less than size , and place all the zero element in temporary array ..........

def move_zero_at_end(array , length ):
	temp_array = [0]*length
	count = 0
	for ele in array:
		if ele !=0:
			temp_array[count] = ele
			count +=1
	while count < length:
		temp_array[count] = 0
		count +=1
	return temp_array
	
	


# ==================Approach 2 =======================
#step 1 :- initialize count with 0
#step 2 :- iterate over the array , 
#step 3 :- if non zero element is found  place current element and place of count and then increment the count 
#step 4 :- Now all non zero element are at the right most of the array , iterate with condition till your count is less than len of array an then place 0 

def move_zero_at_end_without_extra_space(array ,length):
	count = 0 
	for i in array :
		if i !=0 :
			array[count] = i
			count +=1
	while count <length:
		array[count] = 0
		count +=1
	return array

if __name__ == "__main__":
	length = int(input("Enter the Length of an Array : "))
	array = []
	for ele in range(0 , length):
		element = int(input("Enter your Element : "))
		array.append(element)
	result = move_zero_at_end(array , length )
	print("resultant array :" , result)
	print()
	print("============================================")
	print()
	re = move_zero_at_end_without_extra_space(array ,length)
	print("Without extra spaces : ", re)
