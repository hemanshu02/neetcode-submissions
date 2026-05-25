class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res={}
        for i,j in enumerate(nums):
            
            next_value=target-j

            if res.get(next_value) is not None:
                return [res[next_value],i]
            else:
                res[j]=i
        return None
        


