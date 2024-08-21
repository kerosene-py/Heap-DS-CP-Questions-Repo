from collections import Counter
import heapq

def solve(arr):
    freq = Counter(arr)
    h = []
    for key, val in freq.items():
        heapq.heappush(h, (val, -key))

    return [-i[1] for i in h]


arr = list(map(int, input().split()))
print(*solve(arr))