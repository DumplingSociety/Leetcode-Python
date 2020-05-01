def twoSum( nums, target):
    for i, num in enumerate(nums): # adds a counter to an iterable and returns it in a form of enumerate object | 0 - 2 , 1 - 7 , 2 - 11, 3 - 15
        for j in range(i +1, len(nums)): #  range() is used when a user needs to perform an action for a specific number of times  | 1 2 3, 2 3, 
            if num + nums[j] == target: # 2 + 7... 2 + 11... 2 + 15..., 7 + 
                return [i, j]
