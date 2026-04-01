#Cach 1:
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

#Cach 2
def twoSum(nums, target):
    dics = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dics:
            return [dics[complement], i]
        dics[nums[i]] = i