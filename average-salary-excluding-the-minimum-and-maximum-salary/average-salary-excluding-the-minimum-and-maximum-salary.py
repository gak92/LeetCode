class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal = sys.float_info.max
        max_sal = sys.float_info.min
        summ = 0
        
        for sal in salary:
            if sal < min_sal:
                min_sal = sal

            if sal > max_sal:
                max_sal = sal

            summ += sal

        avg = (summ - min_sal - max_sal) / (len(salary) - 2)
        return avg