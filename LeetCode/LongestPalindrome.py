class Palindrome:
     def __init__(self, length, value):
         self.length = length
         self.value = value
          
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 1:
          return s
        maxPalindrome = Palindrome(1, s[0])
        #Take 2 simbols and check if it is palyndrome
        # if it check than it is a part of bigger palindrom
        # if not do the same with 3 symbols
        
        for i in range(0, length-1):
          p2 = self.getMaxLength(s, i, 2)
          if (p2.length > maxPalindrome.length):
            maxPalindrome.length = p2.length
            maxPalindrome.value = p2.value

          p3 = self.getMaxLength(s, i, 3)
          if (p3.length > maxPalindrome.length):
            maxPalindrome.length = p3.length
            maxPalindrome.value = p3.value

        return maxPalindrome.value

    def getMaxLength(self, s, i, m):
      palindrome = Palindrome(1, s[i])
      subStr = s[i:i+m]
      if self.isPalindrome(subStr):
          palindrome.length = m
          palindrome.value = subStr
          j = i
          k = i + m
          while (j >= 0 and k <= len(s)):
              if not self.isPalindrome(s[j:k]):
                  break            
              palindromValue = s[j:k]
              key = len(palindromValue)
              if (key > palindrome.length):
                palindrome.length = key
                palindrome.value = palindromValue
              j -= 1
              k += 1
      return palindrome

    def isPalindrome(self, s):
        return self.reverse(s) == s
        
    def reverse(self, s):
        reversed = ""
        for i in range(len(s)-1, -1, -1):
            reversed += s[i]
        return reversed

solution = Solution()
s2 = "aaaa"
print(solution.longestPalindrome(s2))