# Remove all occurance of target element 

def remove_all_occurance(array,target, length):
	temp_array = [0]*length
	count = 0 
	for ele in array:
		if ele !=target:
			temp_array[count] = ele 
			count +=1
	return temp_array , count

if __name__ == "__main__":
	length = int(input("Enter the length of the array : "))
	target = int(input("Enter the target element : "))
	array = []
	for ele in range(0,length):
		element = int(input("Enter the element: "))
		array.append(element)
	result = remove_all_occurance(array,target , length)
	print("Resultant array : ", result) 
