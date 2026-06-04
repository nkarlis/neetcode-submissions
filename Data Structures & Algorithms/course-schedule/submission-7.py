class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sche = [[] for i in range(numCourses)]

        for crs, pre in prerequisites:
            sche[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if sche[crs] == []:
                return True
            visit.add(crs)

            for pre in sche[crs]:
                if not dfs(pre):
                    return False
            sche[crs] = []
            visit.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True 