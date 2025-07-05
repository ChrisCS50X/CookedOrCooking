from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = []
        freq = Counter(arr)

        for k,v in freq.items():
            if (k == v):
                res.append(v)

        return max(res) if res else -1