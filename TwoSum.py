# encoding=utf-8
import time

# def solution(nums, target):
#     for i, val in enumerate(nums):
#     # for i in range(len(nums)):
#         m = i + 1
#         while m < len(nums):
#             num = nums[m]
#             if (val+num == target):
#                 return [i,m]
#             else:
#                 m = m + 1

def solution(nums,target):
    length = len(nums)
    for i in range(length):
        nums_2 = nums[i:]
        length2 = len(nums_2)
        for j in range(length2):
            if (nums[i] + nums[j] == target):
                return [i, j]

if __name__ == "__main__":
    array = [3,2,4]
    target = 6
    tricks = time.time();
    print tricks
    print solution(array, target)
    print time.time() - tricks