def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num

    return result

# Test the function with the example given
nums = [2, 2, 1]
result = singleNumber(nums)
print(result)
