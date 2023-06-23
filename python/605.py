from typing import List


class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    placeFlowersCount = 0
    adjacent = False
    empty = False
    for f in flowerbed:
      if f == 1:
        adjacent = True
        empty = False
      else:
        if adjacent:
          adjacent = False
        else:
          if empty:
            placeFlowersCount = placeFlowersCount + 1
            empty = False
          else:
            empty = True
    if adjacent == False and empty == True:
      placeFlowersCount = placeFlowersCount + 1
    print(placeFlowersCount)
    if n <= placeFlowersCount:
      return True
    return False


s = Solution()
print(s.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(s.canPlaceFlowers([1, 0, 0, 0, 1], 2))
print(s.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
print(s.canPlaceFlowers([0, 0, 1, 0, 0, 0, 0, 1], 2))
