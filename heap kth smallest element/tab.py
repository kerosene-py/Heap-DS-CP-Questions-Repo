import heapq

def solve(arr, k):
    n = len(arr)
    
    ans = []
    for i in range(n):
        heapq.heappush(ans, -arr[i])
        if len(ans) > k:
            heapq.heappop(ans)
    return -heapq.heappop(ans)


k = int(input())
arr = list(map(int, input().split()))
print(solve(arr, k))