class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        intervals.sort(key = lambda x:x[0])
        currentinterval = intervals[0]
        outputarray = []
        outputarray.append(currentinterval)
        for interval in intervals[1:]:
            currentbegin= currentinterval[0]
            currentend = currentinterval[1]
            nextbegin = interval[0]
            nextend = interval[1]
            if currentend >= nextbegin:
                currentinterval[1]= max(currentend,nextend)
            else:
                currentinterval = interval
                outputarray.append(currentinterval)
        return outputarray
        
        
        
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
