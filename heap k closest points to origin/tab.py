import heapq


def solve(arr, n, k):
    ans = []
    for i in range(n):
        x, y = arr[i]
        heapq.heappush(ans, (-(x**2 + y**2), (x, y)))
        if len(ans) > k:
            heapq.heappop(ans)
    
    return [t[1] for t in ans]
    
    
arr = []
n = int(input())
k = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
print(*solve(arr, n, k))