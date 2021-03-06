# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DIR = [(0, 1), (1, 0)]
        isValid = lambda move: 0 <= move[0] < m and 0 <= move[1] < n
        
        # visited = {}
        @lru_cache
        def dfs(node):
            if not isValid(node):
                return 0
            elif node == (m-1, n-1):
                return 1
            # elif node in visited:
            #     return visited[node]
            
            rnxt = (node[0]+0, node[1]+1)
            bnxt = (node[0]+1, node[1]+0)
            # visited[node] = dfs(rnxt) + dfs(bnxt)
            # return visited[node]
            return dfs(rnxt) + dfs(bnxt)
 
        return dfs((0, 0))


# time O(mn)
# space = O(mn)

        
