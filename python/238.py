from typing import List


class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    last = 1
    result = [1] * len(nums)

    for i in range(1, len(nums)):
      result[i] = result[i - 1] * nums[i - 1]

    for i in range(len(nums) - 2, -1, -1):
      last = last * nums[i + 1]
      result[i] = result[i] * last

    return result


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
