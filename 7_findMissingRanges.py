def findMissingRanges(nums, lower, upper):
    result = []

    # Helper function to add ranges to the result
    def addRange(start, end):
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + '->' + str(end))

    # Check for missing numbers before the first element
    if lower < nums[0]:
        addRange(lower, nums[0] - 1)

    # Check for missing numbers between consecutive elements
    for i in range(len(nums) - 1):
        if nums[i] + 1 < nums[i + 1]:
            addRange(nums[i] + 1, nums[i + 1] - 1)

    # Check for missing numbers after the last element
    if nums[-1] < upper:
        addRange(nums[-1] + 1, upper)

    return result

nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
print(result)
