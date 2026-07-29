class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1 = 0
        r1 = len(matrix)-1

        while l1 <= r1:
            m1 = (r1 + l1)//2

            if matrix[m1][-1] > target and matrix[m1][0] < target:
                l2 = 0
                r2 = len(matrix[m1])-1

                while l2 <= r2:

                    m2 = (r2+l2)//2

                    if matrix[m1][m2] < target:
                        l2 = m2 + 1 
                    elif matrix[m1][m2] > target:
                        r2 = m2 - 1
                    else:
                        return True
                return False

            elif matrix[m1][0] > target:
                r1 = m1 - 1

            elif matrix[m1][-1] < target:
                l1 = m1 + 1

            else:
                return True

        return False
