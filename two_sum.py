# Solution accepted; runtime = 48 ms
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Grab a reference to the original index of each number in nums
        original_indices = {}

        for i, num in enumerate(nums):
            original_indices[num] = list()

        # Handle the fact that we may see a value more than once in the list
        for i, num in enumerate(nums):
            original_indices[num].append(i)

        # See what we need to search for for each number in nums
        deltas = [(target - x, i) for i, x in enumerate(nums)]

        for i, delta in enumerate(deltas):
            '''
            If the delta we are looking for is in the array of input numbers,
            and nums[i] only appears once in nums, and the delta is not equal to⁠
            the singular occurrence of the number itself, we want to return
            this i, and the index corresponding to the delta value in nums
            '''
            if delta[0] in original_indices.keys() and nums[i] != delta[0]:
                return([i, original_indices[delta[0]][0]])

            '''
            # If the delta we are looking for is in the array of input numbers,
            and nums[i] appears MORE THAN ONCE in nums, we want to return this
            i, and the index corresponding to the delta value (which == nums[i])
            in nums
            '''
            elif delta[0] in original_indices.keys() and len(original_indices[delta[0]]) >1:
                return([i, original_indices[delta[0]][1]])
