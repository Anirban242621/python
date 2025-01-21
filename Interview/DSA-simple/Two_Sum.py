# # EXAMPLE:
# #     Input : nums=[2,11,7,15]
# #             target = 9
# #     Output : [0,2]
# #     Explanation : Because nums[0]+nums[2]==9, return [0,2]
# def twoSum(nums,target):
#     hash_map={}
#     for i,v in enumerate(nums):
#         if target-v in hash_map:
#             return( i, hash_map[target-v])
#         else:
#             hash_map[v]=i
#     return []

# nums=[11,7,15,2]
# target=9
# a=twoSum(nums,target)
# print(list[a])


def twoSum(nums,target):
    hash_map={}
    for i,v in enumerate(nums):
        print(i)
        print(v)
        if target-v in hash_map:
            return( i, hash_map[target-v])
        else:
            hash_map[v]=i
    return []

nums=[11,7,15,2]
target=9
a=twoSum(nums,target)
for i in nums,a:
    print(nums[i])
