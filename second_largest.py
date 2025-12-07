# Find the second largest element in the array 

#============Approach 1 =============
#============ Sort the Array  and return the element at position len(array)-2
#----------time complexity O(n log(n))

def brut_second_largest(arr):
	size = len(arr)
	arr.sort()
	return arr[size-2]
	
	
#============ Optimal code comparing with two veriable largest and second largest ===
#------------time complexity O(n)

from math import inf
def opti_second_largest(arr):
	size = len(arr)
	largest = -inf
	second_largest = -inf
	for ele in arr:
		if ele >largest:
			second_largest = largest
			largest = ele
		else:
			if ele != largest and ele > second_largest:
				second_largest = ele
	return second_largest

if __name__ == '__main__':
	arr = []
	size = int(input("Enter length of array"))
	for ele in range(0 ,size):
		element = int(input("Enter element in array"))
		arr.append(element)
	print("Input Array", arr)
	brutresult = brut_second_largest(arr)
	print("Brut Force - Result", brutresult)
	print()
	print("======================================")
	optimalresult = opti_second_largest(arr)
	print("Optimal - Result", optimalresult)
