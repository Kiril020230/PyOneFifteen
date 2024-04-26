import random
nums = [random.randint(-100, 100) for _ in range(20)]
print("Исходный список:")
print(nums)

maxi = nums.index(max(nums))
nums[0], nums[maxi] = nums[maxi], nums[0]

print("Список до/после замены:")
print(nums)