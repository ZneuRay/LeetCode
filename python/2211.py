from typing import List


class Solution:
  def countCollisions(self, directions: str) -> int:
    newDirections = []
    collideCount = 0
    rCount = 0
    for i in range(len(directions)):
      d = directions[i]
      newDirections.append(d)
      if d == 'R':
        rCount = rCount + 1
        continue
      elif d == 'L':
        if i == 0:
          continue
        if newDirections[i - 1] == 'R':
          collideCount = collideCount + rCount + 1
          rCount = 0
          newDirections[i] = 'S'
          newDirections[i - 1] = 'S'
        elif newDirections[i - 1] == 'S':
          collideCount = collideCount + 1
          newDirections[i] = 'S'
      else:
        if i == 0:
          continue
        if newDirections[i - 1] == 'R':
          collideCount = collideCount + rCount
          rCount = 0
          newDirections[i - 1] = 'S'
    return collideCount


s = Solution()
s.countCollisions("RLRSLL")
s.countCollisions("LLRR")
s.countCollisions("RRLL")
