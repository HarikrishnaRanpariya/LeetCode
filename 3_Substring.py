"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", which the length is 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt=0
        Fcnt=0
        Olist=[]
        Tlist=[]
        
        Olist=list(s)
        while Olist:
            
            var = Olist.pop(0)
            
            if var in Tlist:
                cnt=len(Tlist)
                if Fcnt < cnt:
                    Fcnt = cnt
                del Tlist[:Tlist.index(var)+1]
            
            Tlist.append(var)
        
        cnt=len(Tlist)
        if Fcnt < cnt:
            Fcnt = cnt
        
        return Fcnt

def main():
	s = input("Please enter string: ")
	obj = Solution()
	print("Longest substring of \"%s\" is %d" %(s,obj.lengthOfLongestSubstring(s)))

main()
