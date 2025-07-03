class SolutionBruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)-1):
            for j in range (i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]
                
class SolutionHashMap:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Kita bikin dulu hashmap kosong buat nyimpen elemen array yang udah kita lewatin isinya val : index
        prevArr = {} 

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevArr:
                return [prevArr[diff],i]
            # Disini kita decide kalau value yang akan point ke index
            prevArr[n] = i
        return 