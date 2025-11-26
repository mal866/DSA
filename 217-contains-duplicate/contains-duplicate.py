class Solution(object):
    def containsDuplicate(self, nums):
        hashmap = {}
        output = "false"
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                return True
        return False
        