class Solution:
    def isPalindrome(self, s: str) -> bool:

        alphaNumStr = ""
        for ch in s:
            isSmallCase = ord(ch) >= ord('a') and ord(ch) <= ord('z')
            isBigCase = ord(ch) >= ord('A') and ord(ch) <= ord('Z')
            isNum = ord(ch) >= ord('0') and ord(ch) <= ord('9')
            
            if (isSmallCase or isBigCase or isNum):
                alphaNumStr += ch.lower()
        
        length = len(alphaNumStr)
 
        for i in range(int(length / 2)):
            j = length - i - 1

            if (alphaNumStr[i] != alphaNumStr[j]):
                return False
        
        return True
        
        