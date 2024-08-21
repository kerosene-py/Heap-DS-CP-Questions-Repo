
# Input: 6 5 3 2 8 10 9
        #  k = 3
# Output: 2 3 5 6 8 9 10

# Explaination: every element k steps right left.

import heapq


def solve(arr, k):
    n = len(arr)
    ans = []
    
    for i in range(k): heapq.heappush(ans, arr[i])
    for i in range(n):
        if i+k < n:
            heapq.heappush(ans, arr[i+k])
        arr[i] = heapq.heappop(ans)
        
    return arr


k = int(input())
arr = list(map(int, input().split()))
print(*solve(arr, k))