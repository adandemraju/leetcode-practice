'''
You are given an array of integers heights where heights[i]
represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be 
formed among the bars. Note: This chart is known as a 
histogram.

Example 1:
Input: heights = [7,1,7,2,2,4]
Output: 8

Example 2:
Input: heights = [1,3,7]
Output: 7

Constraints:
1 <= heights.length <= 100,000.
0 <= heights[i] <= 10,000
'''

from ast import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #keep track of heights using a stack
        #ex. [7,1,7,2,2,4]
            #add 7 to stack, compare next height with stack, if stack is higher move to next height, move left pointer
            #keep track of left and right pointers to get width

        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea