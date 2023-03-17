# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:39:48 2023

@author: User
"""


import collections

grid = [["1", "1", "1", "1", "1", "1"],
        ["1", "1", "0", "0", "0", "0"],
        ["0", "0", "0", "1", "1", "1"],
        ["0", "0", "0", "1", "1", "1"],
        ["0", "0", "1", "0", "0", "0"],   
        ["1", "0", "0", "0", "0", "0"]
]

queries = [6, 1, 8, 2]


def onesGroups(grid, queries) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        visited_elt = set()
        directions = [[1,0],
                      [-1,0],
                      [0,1],
                      [0,-1]]

        solution = []

        def bfs(row, col):
            area = 0
            queue = collections.deque()
            visited_elt.add((row, col))
            queue.append((row, col))
            area += 1

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited_elt):
                         queue.append((r,c))
                         visited_elt.add((r,c))
                         area += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited_elt:
                    solution.append(bfs(row, col)) 
        
        result = [] 
        for i in range(len(queries)):
            count = 0 
            for j in range(len(solution)):
                if solution[j] == queries[i]:
                    count += 1
            result.append(count)    
                   
        return result    
    
onesGroups(grid, queries)       













