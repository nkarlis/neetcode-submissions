class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = [[] for _ in range(numCourses)]
        for pre, crs in prerequisites:
            preMap[pre].append(crs)
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True
            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            preMap[crs] = []
            visiting.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

