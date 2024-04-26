nums = [float(input(f"Введите число {i+1}: ")) for i in range(15)]
maxi = nums.index(max(nums))
nums[-1], nums[maxi] = nums[maxi], nums[-1]

print("Список после замены наибольшего элемента с последним:", nums)