def smallest_missing_positive_integer(nums: list[int]) -> int:
    nums = [num for num in nums if num > 0]
    
    n = len(nums)
    for i in range(n):
        if abs(nums[i]) - 1 < n and nums[abs(nums[i]) - 1] > 0:
            nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
    

    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    return n + 1







    



  

