def subarraySum(nums, k):
    d = {}
    prefix_sum = 0
    count = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
        if prefix_sum == k:
            count += 1
        if prefix_sum - k in d:
            count += d[prefix_sum - k]
        d[prefix_sum] = d.get(prefix_sum, 0) + 1
    return count