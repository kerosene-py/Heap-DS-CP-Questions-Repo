
# Input: 5 6 7 8 9 (k=3)
# Output: 7

# Explaination:

import heapq


def solve(arr, k, x):
    h = []
    for i in range(len(arr)):
        heapq.heappush(h, (-abs(x - arr[i]), arr[i]))
        if len(h) > k:
            heapq.heappop(h)
            
    return [i[1] for i in h]
            


x = int(input())
k = int(input())
arr = list(map(int, input().split()))
print(*solve(arr, k, x))