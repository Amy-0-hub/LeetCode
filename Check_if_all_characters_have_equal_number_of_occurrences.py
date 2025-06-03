class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict1 = {}
        for element in s:
            if element in dict1:
                dict1[element] += 1
            else:
                dict1[element] = 1
        if len(set(dict1.values())) == 1:
            return True
        else:
            return False


# test case
## case 1 : 'abacbc'
## case 2: '1'

string1 = "abacbc"
string2 = "1"

s = Solution()
print(s.areOccurrencesEqual(string1))
print(s.areOccurrencesEqual(string2))
