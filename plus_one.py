from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        large_int_str = ''.join(map(str,digits))    #join method expects a sequence of strings
        # print(large_int_str)
        # print(type(large_int_str))
        large_int = int(large_int_str) + 1
        # print(large_int)
        # print(type(large_int))
        convert_list = list(map(int, str(large_int)))   # convert to string, integer can't iterable
        # print(convert_list)
        return convert_list




# case test
digits = [1,2,3, 4]
s = Solution()
print(s.plusOne(digits))
