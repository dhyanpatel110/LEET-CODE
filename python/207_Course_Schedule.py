'''
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''

#CODE:
  class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #each course to prereqisite list
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        #visitSet = all course algo the curr dfs path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
                
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False 
            visitSet.remove(crs)
            preMap[crs] = []
            return True
            
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
            
                    
            
