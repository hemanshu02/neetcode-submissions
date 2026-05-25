class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i in strs:
            x="".join(sorted(i))
            if x not in res:
                res[x] = []
            res[x].append(i)
        result=[]
        for x,y in res.items():
            result.append(y)
        return result