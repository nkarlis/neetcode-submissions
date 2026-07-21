class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        path = set()
        def dfs(crs):
            if crs in path:
                return False
            if preMap == []:
                return True
            path.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True