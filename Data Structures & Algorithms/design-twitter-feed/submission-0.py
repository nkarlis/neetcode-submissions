class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result = []

        users = self.followMap[userId] | {userId}

        for uid in users:
            tweets = self.tweetMap[uid]
            if tweets:
                index = len(tweets) - 1
                timestamp, tweetId = tweets[index]
                heap.append((timestamp, tweetId, uid, index))

        heapq.heapify_max(heap)

        while heap and len(result) < 10:
            _, tweetId, uid, index = heapq.heappop_max(heap)
            result.append(tweetId)

            # Add this user's next older tweet.
            if index > 0:
                index -= 1
                timestamp, tweetId = self.tweetMap[uid][index]
                heapq.heappush_max(
                    heap, (timestamp, tweetId, uid, index)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
