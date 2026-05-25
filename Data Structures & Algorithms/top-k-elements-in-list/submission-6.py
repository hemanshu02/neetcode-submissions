class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={}
        for i in nums:
            res[i]=res.get(i,0)+1
        res=sorted(res.items(),key=lambda kv : (kv[1],kv[0]),reverse=True)
        res=[x[0] for x in res[0:k]]
        return res
        

        