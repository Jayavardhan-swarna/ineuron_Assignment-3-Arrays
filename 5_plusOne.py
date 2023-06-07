def plusOne(digits):
    n = len(digits)
    carry = 1  # Initialize the carry as 1 to increment by one

    for i in range(n - 1, -1, -1):
        digits[i] += carry

        if digits[i] < 10:
            # No carry, so we can stop and return the updated array
            return digits
        else:
            # Carry occurred, so set the current digit to 0
            digits[i] = 0

    # If the loop completes without returning, it means there is still a carry
    # We need to insert a new most significant digit 1 at the beginning
    return [1] + digits

digits = [1, 2, 3]
result = plusOne(digits)
print(result)
