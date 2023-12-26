class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack=[]
        l=[]
        for i in range(0,len(t)):
            stack=[t[i]]
            while t[i]<stack[-1]:
                stack.append(t[i])
                i+=1
            l.append(len(stack))
    
        return l   