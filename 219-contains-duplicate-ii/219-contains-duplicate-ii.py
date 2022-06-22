class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:   
        hmap = {}
        for i,v in enumerate(nums):
            if v in hmap and i - hmap[v] <= k:
                return True
            hmap[v] = i
        return False 