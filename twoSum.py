"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

# 1st approch
# The brute force approach is simple. Loop through each element xx and find if there is another value that equals to target - xtarget−x.
# 1. Time: O(n^2), Space: O(1)
def twoSum( nums, target):
    for i, num in enumerate(nums): # adds a counter to an iterable and returns it in a form of enumerate object | 0 - 2 , 1 - 7 , 2 - 11, 3 - 15
        for j in range(i +1, len(nums)): #  range() is used when a user needs to perform an action for a specific number of times  | 1 2 3, 2 3, 
            if num + nums[j] == target: # 2 + 7... 2 + 11... 2 + 15..., 7 + 
                return [i, j]


# Drive
print (twoSum([2,7,11,15],26))


'''
Approach 3: One-pass Hash Table
It turns out we can do it in one-pass. While we iterate and inserting elements into the table, 
we also look back to check if current element's complement already exists in the table. 
If it exists, we have found a solution and return immediately.

Time complexity : O(n)O(n). We traverse the list containing nn elements only once. Each look up in the table costs only O(1)O(1) time.

Space complexity : O(n)O(n). The extra space required depends on the number of items stored in the hash table, which stores at most nn elements.
'''
 
#.If we look for a value we track the index of that value when it first appears.
# As soon as you find the values that satisfy the problem you are done. The time on this is also O(N)
# Runtime: 40 ms
class Solution:
    def twoSum(self, nums, target):
        look_for = {}
        for n, x in enumerate(nums): #  n - x : 0 - 1 , 1 - 3 , 2 - 5, 4 - 7
           # print(n, x) # first {}, second {5:0}, 3rd {5: 0, 3: 1}
            try:       
                return look_for[x], n # look_for[1], 0 triger KeyError, since look_for is emp dict
            except KeyError:
                look_for.setdefault(target - x,n) # dict.setdefault(key, default) Key- is the key to be searched , 
                                                  # defult- this is the value to be returnd in case key is not found
                                                  # key = 6-1 = 5, defult = n = 0. search 5 , return 0 
              #  print(target - x, n) # 5, 0 add to look_for; add 3: 1 to look_for
             #   print(look_for)

test_case = Solution()
array = [1,3, 5, 7]
array2 = [3,2,4]
given_nums=[2,7,11,15]
#print(test_case.twoSum(array, 6))  # 0 2
#print(test_case.twoSum(array2, 6))
#print(test_case.twoSum(given_nums,89)) # (0, 1)

# similary solution use dict as hashtable
class Solution:
   def twoSum(self, nums, target):
       """
       :type nums: List[int]
       :type target: int
       :type: List[int]
       """
       nums_dict = {}
       for i, n in enumerate(nums): 
           if((target - n) in nums_dict.keys()):
               return [nums_dict[target - n], i]
           nums_dict[n] = i      
           
           
           
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Hash Map to store the number and id
        m = {}
        for i,n in enumerate(nums):  # enumerate(iterable, start=0) Iterable: any object that supports iteration, Start: the index value from which the counter is 
                                       # to be started, by default it is 0 
           # print(i, n) # i, n -> 0 1 , 1 3 , 2 5
            if (target - n) in m:  # if 6-1 = 5 in m , retrun m[5, 0]
                return (m[target-n],i)
            else:                   # if not , m[1] = 0
                m[n] = i
        return []

test_case = Solution()
array = [1, 3, 5, 7]
print(test_case.twoSum(array, 8))