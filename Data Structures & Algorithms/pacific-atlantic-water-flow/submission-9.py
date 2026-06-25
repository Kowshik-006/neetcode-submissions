class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        pacific, atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        
        def dfs(row, col, visited, prevVal):
            if ((row,col) in visited) or row < 0 or row == rows or col < 0 or col == cols or heights[row][col] < prevVal:
                return
            visited.add((row,col))
            for dr,dc in directions:
                dfs(row+dr,col+dc,visited,heights[row][col])
        
        for col in range(cols):
            dfs(0,col,pacific,heights[0][col])
            dfs(rows-1,col,atlantic,heights[rows-1][col])
        
        for row in range(rows):
            dfs(row,0,pacific,heights[row][0])
            dfs(row,cols-1,atlantic,heights[row][cols-1]) 
        
        for tup in pacific:
            if tup in atlantic:
                result.append(list(tup))
            
        return result