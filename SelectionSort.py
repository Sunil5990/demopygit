
def SelectionSort(nums):
    for i in range(len(nums)-1):
        min_pos=i
        for j in range(i,len(nums)):
            if nums[j]<nums[min_pos]:
                min_pos=j
        nums[min_pos],nums[i]=nums[i],nums[min_pos]
        print(nums)



nums=[5,8,9,3,4,2,10,6]
SelectionSort(nums)
print(nums)