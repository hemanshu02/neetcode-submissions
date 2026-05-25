class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=s.lower()
        t=t.lower()
        if len(s) != len(t):
            return False
        dic_s={}
        dic_t={}
        for i in range(len(s)):
            dic_s[s[i]]=dic_s.get(s[i],0)+1
            dic_t[t[i]]=dic_t.get(t[i],0)+1
        for i in dic_s.keys():
            try:

                if  dic_s[i] != dic_t[i]:
                    return False
            except:
                return False
        return True


        