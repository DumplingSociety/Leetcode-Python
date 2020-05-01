'''
Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_l = 0

        for pts in range(1, len(s)):
            if(s[pts] in s[start:pts]):
                max_l = len(s[start:pts]) if (len(s[start:pts]) > max_l) else max_l
                start = s[start:pts].index(s[pts]) + 1 + start
            else:
                if(pts == len(s) - 1):
                    max_l = max([max_l, len(s[start:])])

        return max_l if(max_l != 0) else len(s)
    
# Function to find and print longest  
# substring without repeating characters.  
def findLongestSubstring(string): 
  
    n = len(string)  
  
    # starting point of current substring.  
    st = 0
  
    # maximum length substring without  
    # repeating characters.  
    maxlen = 0
  
    # starting index of maximum  
    # length substring.  
    start = 0
  
    # Hash Map to store last occurrence  
    # of each already visited character.  
    pos = {}  
  
    # Last occurrence of first 
    # character is index 0  
    pos[string[0]] = 0
  
    for i in range(1, n):  #  range() allows user to generate a series of numbers within a given range # n = 13, 1 - 12 
        # If this character is not present in hash,  
        # then this is first occurrence of this  
        # character, store this in hash.  
        if string[i] not in pos:  # if string[1] not in pos
            pos[string[i]] = i  # pos[E] = 1
  
        else: 
            # If this character is present in hash then  
            # this character has previous occurrence,  
            # check if that occurrence is before or after  
            # starting point of current substring.  
            if pos[string[i]] >= st:
                print('first: ', pos[string[i]])
                print('start point', st)
              
  
                # find length of current substring and  
                # update maxlen and start accordingly.  
                currlen = i - st  
                print('currlen: ', currlen, i , st)
                if maxlen < currlen:  
                    maxlen = currlen  
                    start = st  
  
                # Next substring will start after the last  
                # occurrence of current character to avoid  
                # its repetition.  
                st = pos[string[i]] + 1
                print('st: ',st)
              
            # Update last occurrence of  
            # current character.  
            pos[string[i]] = i 
            print('pos: ', pos[string[i]],i) 
          
    # Compare length of last substring with maxlen  
    # and update maxlen and start accordingly.  
    if maxlen < i - st: 
        maxlen = i - st  
        start = st 
        print('start2if : ', maxlen)  
      
    # The required longest substring without  
    # repeating characters is from string[start]  
    # to string[start+maxlen-1].  
    
    print(pos)
    print('start: start + maxlen', start ,start + maxlen)
    return string[start : start + maxlen]  
  
# Driver Code 
if __name__ == "__main__":  
  
    string = "GEEKSFORGEEKST"
    print(findLongestSubstring(string))  
  
# This code is contributed by Rituraj Jain 