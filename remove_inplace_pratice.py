class Solution:
    def __init__(self):
        pass

    def removeDuplicates(self, numbers: list[int]) -> int:
        ptr_read, ptr_write = 1, 1
        for ptr_read in range(1, len(numbers)):
            if numbers[ptr_read] != numbers[ptr_read - 1]:
                numbers[ptr_write] = numbers[ptr_read]
                ptr_write += 1

        return ptr_write

    def function_1(self) -> None:
        pass


numbers_1 = [1, 2, 3, 3, 4, 5, 6]

k = Solution().removeDuplicates(numbers_1)
print(numbers_1)
print(k)

# 创建instance，并且调用这个instance的一个method
# s1 = Solution()
# s1.function_1()

# OOP
# What is class
# 模版，用来描述一类事物
# What is instance / object, and the constructor
# 模版的具像化，实例化。每个instance都会具备模版里定义的属性
# 带有self的属性函数，只能被instance调用，也就是说，必须先创建instance，再调用函数
# 构造函数，如果不提供，那么为空（pass）


# in place operation
# k = Solution().removeDuplicates(numbers_1)
# expect k = 5, numbers_1 = [1, 2, 3, 4, 5, _]

# not in place operation
# return_1 = Solution().removeDuplicates(numbers_1)
# expect numbers_1 = [1, 2, 3, 3, 4, 5]
# return_1 = [1, 2, 3, 4, 5, _]
