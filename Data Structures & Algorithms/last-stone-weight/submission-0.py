class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # sort data into maxHeap
        negHeap = [-s for s in stones]
        heapq.heapify(negHeap)

        while len(negHeap) > 1:
            first = -1 * heapq.heappop(negHeap) #6
            second = -1 * heapq.heappop(negHeap) #4

            if second < first:
                heapq.heappush(negHeap, -1 * (first - second))

        negHeap.append(0)
        return abs(negHeap[0])
        