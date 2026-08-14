class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #area = max(min height * width (right-left)
        #height = min between left and right
        #width = fixed = right - left
        # area = max(area,new_area)

        area = 0

        left,right = 0,len(heights)-1

        while left < right:
            width = right - left
            height = min(heights[left],heights[right])
            area = max(area,width*height)

            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        
        return area
        