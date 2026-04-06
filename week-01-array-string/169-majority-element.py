def majorityElement(nums: list[int]) -> int:
    res = None
    cnt = 0
    for i in nums:
        if cnt == 0:
            res = i    
        if i == res:
            cnt += 1
        else:
            cnt -= 1
    return res
