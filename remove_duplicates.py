#• Remove duplicates from an array without using extra space.

# use sorting function to sort the array 
#use two pointer approach slow and fast 
#iterate over array untill fast moves to end element in the array
#if you find element at slow and elemnt at fast are same , donot remove anything , just increment the fast pointer
#if element at slow and fast are same , increment the slow pointer and copy elemnt for fast pointer into the slow pointer 

#time complexity O(nlog(n))
#space complexity Auxiliary Space:O(log n)O(n)

def optimal_remove_duplicates(nums):
	nums.sort()
	slow = 0
	fast = 1
	while fast<len(nums):
		if nums[slow] == nums[fast]:
			fast +=1
		else:
			if nums[slow] != nums[fast]:
				slow +=1
				nums[slow] = nums[fast]
	return nums[:slow+1]

if __name__ =='__main__':
	size = int(input("Enter size of array"))
	array = []
	for ele in range(0, size):
		element = int(input("Enter element of an array"))
		array.append(element)
	print("Input Array", array)
	optimal_result = optimal_remove_duplicates(array)
	print("==========================================")
	print("Resultant Array ", optimal_result)
