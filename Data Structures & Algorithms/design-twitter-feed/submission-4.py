class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        result, heap = [], []
        users = self.followMap[userId]
        users.add(userId)
        for uid in users:
            tweets = self.tweetMap[uid]
            if tweets:
                index = len(tweets) - 1
                timestamp, tweetId = tweets[index]
                heapq.heappush_max(heap, [timestamp, tweetId, uid, index])
        
        while heap and len(result) < 10:
            _, tweetId, uid, index = heapq.heappop_max(heap)
            result.append(tweetId)
            if index > 0:
                index -= 1
                timestamp, tweetId = self.tweetMap[uid][index]
                heapq.heappush_max(heap, [timestamp, tweetId, uid, index])
        return result

    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followMap[followerId]:
            return
        self.followMap[followerId].remove(followeeId)
        
