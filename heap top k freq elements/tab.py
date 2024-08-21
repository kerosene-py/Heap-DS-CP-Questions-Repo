from collections import Counter
import heapq

def solve(arr, k):
    freq = Counter(arr)
    h = []
    for key, val in freq.items():
        heapq.heappush(h, (val, key))
        if len(h) > k:
            heapq.heappop(h)

    return [i[1] for i in h]


k = int(input())
arr = list(map(int, input().split()))
print(*solve(arr, k))