class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [[] for i in range(numCourses)]

        for n1, n2 in prerequisites:
            pre[n1].append(n2)
        visiting = set()


        def dfs(crs):
            if crs in visiting:
                return False
            if pre[crs] == []:
                return True

            visiting.add(crs)
            for nei in pre[crs]:
                if not dfs(nei):
                    return False
            pre[crs] = []
            visiting.remove(crs)
            return True



        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True