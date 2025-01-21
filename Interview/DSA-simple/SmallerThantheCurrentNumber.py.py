"""Given the array nums fo each nums[i] find out how many numbers in the array are smaller than it. That is for each nums[i] you have to count the number of valid j's such that j!=i and nums[j] < nums[i]
Example=
        input: nums=[8,1,2,2,3]
        output=[4,0,1,1,3]
        Explanation: nums[0] there are four smaller numbers than it (1,2,2 and 3)
                     nums[1] does not exist any smaller number than it.
                     nums[2] there exist one smaller numbers than it (1)
                     nums[4] there exist three smaller numbers than it(1,2 and 2)"""

def SmallerNums(nums):
    temp= sorted(nums)
    d={}
    for i,num in enumerate(temp):
        if num not in d:
            d[num]=i
    ret=[]
    print(d)
    print(temp)
    for i in nums:
        ret.append(d[i])
    return ret

nums=[8,1,2,2,3]
print(SmallerNums(nums))
