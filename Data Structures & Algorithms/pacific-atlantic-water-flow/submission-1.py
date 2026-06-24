class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        rows, cols = len(heights), len(heights[0])
        pac_map = {}
        at_map = {}
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def canPac(row, col, seen = None):
            if pac_map.get((row,col),False):
                return True
            
            if row == 0 or col == 0:
                pac_map[(row,col)] = True
                return True
            
            if not seen:
                seen = set()
            seen.add((row,col))
            
            for dr,dc in directions:
                r = row + dr
                c = col + dc

                if r < 0 or r == rows or c < 0 or c == cols:
                    continue
                if heights[r][c] <= heights[row][col] and (r,c) not in seen:
                    if canPac(r,c,seen):
                        pac_map[(r,c)] = True
                        return True

            return False

        def canAt(row, col, seen = None):
            if at_map.get((row,col),False):
                return True
            
            if row == rows-1 or col == cols-1:
                at_map[(row,col)] = True
                return True
            
            if not seen:
                seen = set()
            seen.add((row,col))
            
            for dr,dc in directions:
                r = row + dr
                c = col + dc

                if r < 0 or r == rows or c < 0 or c == cols:
                    continue
                if heights[r][c] <= heights[row][col] and (r,c) not in seen:
                    if canAt(r,c,seen):
                        at_map[(r,c)] = True
                        return True

            return False
        
        for row in range(rows):
            for col in range(cols):
                print(row,col)
                if canPac(row,col) and canAt(row,col):
                    result.append([row,col])

        return result
