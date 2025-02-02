def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [0, 0, 7]: 
            return True
    return False
nums = list(map(int, input().split()))
print(spy_game(nums))