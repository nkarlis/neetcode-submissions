class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit, cycle = set(), set()
        prereq = {i:[] for i in range(numCourses)}
        output = []

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True


            cycle.add(crs)

            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            prereq[crs] = []
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)

            return True

        for i in range(numCourses):
             if not dfs(i):
                    return []
        return output