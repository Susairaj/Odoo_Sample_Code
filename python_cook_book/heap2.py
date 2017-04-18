import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
print heap
heapq.heapify(heap)
print heap