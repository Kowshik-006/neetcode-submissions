class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        mid = 0
        bottom = m - 1
        
        while top <= bottom:
            mid = (top+bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][n-1]:
                top = mid + 1
            else:
                left = 0
                mid2 = 0 
                right = n -1

                while left <= right:
                    mid2 = (left+right) // 2
                    if target < matrix[mid][mid2]:
                        right = mid2 - 1
                    elif target == matrix[mid][mid2]:
                        return True
                    else:
                        left = mid2 + 1
                return False

        return False