class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for index,i in enumerate(numbers):
            d[i]=index+1
            b=target-i
            try:
                value=d[b]
                if value==index+1:
                    continue
                else:
                    return [value,index+1]

                
            except:
                continue
        return [0,0]
            




        