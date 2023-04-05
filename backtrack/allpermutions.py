def permutations(nums):
    # Recursive function to generate permutations
    def backtrack(first=0):
        # If all elements have been used up, print the permutation
        if first == n:
            print(nums)
        for i in range(first, n):
            # Place the i-th element first in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # Use recursion to generate all permutations starting from the i-th element
            backtrack(first + 1)
            # Undo the last swap to restore the original list
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    backtrack()
permutations([1, 2, 3])
