def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    right_nums,left_nums = [1] * n, [1] * n
    for i in range(1, n):
        left_nums[i] = left_nums[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
        right_nums[i] = right_nums[i+1] * nums[i+1]
    for i in range(n):
        nums[i] = left_nums[i] * right_nums[i]
    return nums