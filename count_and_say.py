class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(1)
        
        convert_to_string = str(n)
        

#step by step
#start to head

        count = 0
        result = ''
        for i in range(1,len(convert_to_string)):
            if convert_to_string[i-1] == convert_to_string[i]:
                count += 1
                result += str(count) + convert_to_string[i-1]
            else:
                count = 1
                result += str(count) + convert_to_string[i-1]
        return result







n=4
e1 = Solution()
print(e1.countAndSay(n))