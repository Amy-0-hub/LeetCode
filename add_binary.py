class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a,2), int(b,2)
        # print(a)
        # print(b)
        sum = a + b
        print(sum)
        print(type(sum))
        # sum = format(str(sum), 'binary')
        # print(sum)
        sum =bin(sum)
        print(sum[2:])
        return sum[2:]

# case test
a = '11'
b = '1'
s = Solution()
s.addBinary(a,b)