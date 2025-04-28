def solve():
 
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    total_sum = sum(nums)
    for num in nums:
        if (total_sum - num) % K == 0:
            print("Yes")
            return
    
    print("No")
solve()
