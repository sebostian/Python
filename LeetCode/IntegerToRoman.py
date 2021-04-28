class Solution:
    def intToRoman(self, num):
        result = ""
        #1000
        c1000 = num // 1000
        r1000 = num % 1000 
        for i in range(0, c1000):
            result += "M"
        
        #100
        c100 = r1000 // 100
        r100 = r1000 % 100
        
        if c100 == 9:
            result += "CM"
        elif c100 == 5:
            result += "D"
        elif c100 == 4:
            result += "CD"
        elif c100 > 5:
            result += "D"
            for i in range(0, c100 - 5):
                result += "C"
        else:
            for i in range(0, c100):
                result += "C"
        #10
        c10 = r100 // 10
        r10 = r100 % 10

        if c10 == 9:
            result += "XC"
        elif c10 == 4:
            result += "XL"
        elif c10 == 5:
            result += "L"
        elif c10 > 5:
            result += "L"
            for i in range(0, c10 - 5):
                result += "X"
        else:
            for i in range(0, c10):
                result += "X"
        #1
        c1 = r10 
        
        if c1 == 9:
            result += "IX"
        elif c1 == 5:
            result += "V"
        elif c1 == 4:
            result += "IV"
        elif c1 > 5:
            result += "V"
            for i in range(0, c1 - 5):
                result += "I"
        else:
            for i in range(0, c1):
                result += "I"
        return result

x = 60
solution = Solution()
print(solution.intToRoman(x))