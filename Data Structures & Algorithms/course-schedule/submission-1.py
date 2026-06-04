class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereq = {c:[] for c in range(numCourses)}

        visit = set()

        for crs, pre in prerequisites:
            prereq[crs].append(pre)



        def dfs(crs):
            if crs in visit:
                return False
            if prereq[crs] == []:
                return True

            visit.add(crs)

            for pre in prereq[crs]:
                if not dfs(pre):
                    return False

            visit.remove(crs)
            prereq[crs] = []
            return True




        for c in range(numCourses):
            if dfs(c) == False:
                return False

        return True
     