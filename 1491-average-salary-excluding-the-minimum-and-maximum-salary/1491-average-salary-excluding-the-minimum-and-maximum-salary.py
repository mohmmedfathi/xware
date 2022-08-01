class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sz = len(salary)
        low  = salary[0]
        high = salary[sz-1]
        avg = 0.0
        for i in salary :
            avg+=i
        avg = avg - (low + high)
        sz = sz - 2
        avg = avg / sz 
        return avg