def pair_sum(arr , target):
	i =0 
	indx =0
	resultant_dictionary = {}
	#for i in range(i ,len(arr)-2):
	while i<len(arr)-1:
		j = i+1
		while j <len(arr):
			if arr[j] != target - arr[i]:
				j +=1
			else:
				if arr[j] == target - arr[i]:
					resultant_dictionary[indx] = (arr[i], arr[j])
					indx +=1
			
			j +=1
		i +=1
	
	return resultant_dictionary

if __name__ == "__main__":
	target = int(input("Enter the Target Element : "))
	leng_of_array = int(input("Enter the lengt of Array : "))
	array = []
	for i in range(0 , leng_of_array):
		element = int(input("Enter the array element : "))
		array.append(element)
	
	result = pair_sum(array, target)
	print("Resultant : ", result)
	
