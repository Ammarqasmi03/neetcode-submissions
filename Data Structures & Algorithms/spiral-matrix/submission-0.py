class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        left = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1

        spiral_elem_list = []

        while left <= right and top <= bottom:

           # left to right along top
            for i in range(left,right+1):
               spiral_elem_list.append(matrix[top][i])

            top += 1

           # top to bottom along right

            for i in range(top,bottom+1):
               spiral_elem_list.append(matrix[i][right])

            right -= 1

            # right to left along bottom
            if top <= bottom:
                for i in range(right,left-1,-1):
                    spiral_elem_list.append(matrix[bottom][i])

                bottom -= 1

            # bottom to top along left
            if left <= right:
                for i in range(bottom,top-1,-1):
                    spiral_elem_list.append(matrix[i][left])

                left += 1


        return spiral_elem_list









        

