import collections

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_freq = collections.Counter(self.nums2)
        
    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]

        self.nums2_freq[old_val] -= 1

        self.nums2[index] += val

        new_val = self.nums2[index]

        self.nums2_freq[new_val] += 1 
        
    def count(self, tot: int) -> int:
        count = 0
        for num1 in (self.nums1):
            complement = tot - num1
            count += self.nums2_freq.get(complement, 0)
        
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)