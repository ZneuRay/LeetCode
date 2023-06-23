from typing import List


class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    for i in range(len(asteroids)):
      if i != 0 and asteroids[i] < 0:
        for j in range(i - 1, -1, -1):
          if asteroids[j] < 0:
            break
          collide = asteroids[i] + asteroids[j]
          if collide == 0:
            asteroids[i] = 0
            asteroids[j] = 0
            break
          elif collide > 0:
            asteroids[i] = 0
            break
          else:
            asteroids[j] = 0

    result = []
    for a in asteroids:
      if a != 0:
        result.append(a)
    return result


s = Solution()
s.asteroidCollision([5, 10, -5])
s.asteroidCollision([8, -8])
s.asteroidCollision([10, 2, -5])
