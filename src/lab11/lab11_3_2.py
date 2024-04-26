nums = [int(input(f"Введите число {i+1}: ")) for i in range(10)]
minimal = nums.index(min(nums))
nums[-1], nums[minimal] = nums[minimal], nums[-1]

print("Список после замены наименьшего элемента с последним:", nums)