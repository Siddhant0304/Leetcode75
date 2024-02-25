'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''
#Solution

class Solution:
    def reverseVowels(self, s: str) -> str:
      
        n= len(s)
        left,right = 0, n-1
        lst = [i for i in s]
        vowels = ['a','e','i','o','u','A','E','I','O','U']

        while (right>left):
            if lst[left] in vowels and lst[right] in vowels:
                lst[left],lst[right]=lst[right],lst[left]
                left+=1
                right-=1

            if lst[left] not in vowels:
                left+=1

            if lst[right] not in vowels:
                right-=1       
                
        return "".join(lst)
        
