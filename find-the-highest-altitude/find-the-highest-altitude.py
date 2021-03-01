class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = 0
        high_alt = 0
        
        for alt in gain:
            curr_alt += alt
            # print(curr_alt)
            high_alt = max(high_alt, curr_alt)
            
        return high_alt 
              