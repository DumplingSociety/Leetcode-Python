"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
def twoSum( nums, target):
    for i, num in enumerate(nums): # adds a counter to an iterable and returns it in a form of enumerate object | 0 - 2 , 1 - 7 , 2 - 11, 3 - 15
        for j in range(i+1, len(nums)): #  range() is used when a user needs to perform an action for a specific number of times  | 1 2 3, 2 3, 
            if num + nums[j] == target: # 2 + 7... 2 + 11... 2 + 15..., 7 + 
                return [i, j]


# Drive
print (twoSum([2,7,11,15],26))

def two_sum(arr,s):
  arr = list(set(arr)) #remove duplicates
  hashtable = {}
  ans = {}
  for i in arr:
    k = s - i
    if k not in hashtable:
      hashtable[i] = k
    else:
      hashtable[i] = k
      ans.append([d[k],d[i]])
  
  return ans

print (twoSum([2,7,11,15],26))
'''
range(start, stop, step) takes three arguments.

print('i: ', i)
print('len(nums): ', len(nums))

range()
for i in range(10): 
    print(i, end =" ") 
    
print() 
0 1 2 3 4 5 6 7 8 9 

for i in range(1, 11): 
    print(i, end =" ") 
1 2 3 4 5 6 7 8 9 10 


for i in range(4, 4): 
    print(i, end =" ") # nothing
 
'''

