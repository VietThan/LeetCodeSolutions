import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        n = len(obstacles)
        answer = [1] * n
        
        # lis[i] records the lowest increasing sequence of length i + 1.
        lis = []
    
        for i, height in enumerate(obstacles):
            # Find the rightmost insertion position idx.
            idx = bisect.bisect_right(lis, height)
            
            if idx == len(lis):
                lis.append(height)
            else:
                lis[idx] = height
            answer[i] = idx + 1
            
        return answer
    
def main():
    obstacles1 = [1,2,3,2]
    result1 = [1,2,3,3]

    obstacles2 = [2,2,1]
    result2 = [1,2,1]

    obstacles3 = [3,1,5,6,4,2]
    result3 = [1,1,2,3,2,2]

    sol = Solution()
    attempt1 = sol.longestObstacleCourseAtEachPosition(obstacles1)
    assert attempt1 == result1

    attempt2 = sol.longestObstacleCourseAtEachPosition(obstacles2)
    assert attempt2 == result2

    attempt3 = sol.longestObstacleCourseAtEachPosition(obstacles3)
    assert attempt3 == result3

if __name__ == "__main__":
    main()