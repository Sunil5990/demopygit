
def BubbleSort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
        print(list)


nums=[5,3,8,6,7,2]
BubbleSort(nums)
print(nums)