class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        res = []
        
        for num in nums1:
            dic[num] = 1
            
        for num in nums2:
            if num in dic:
                dic[num] = 2
                
        for num in dic:
            if dic[num] == 2:
                res.append(num)
            
        return res
        
        
#         intersect = []
#         l1 = len(nums1)
#         l2 = len(nums2)
#         if l1 < l2:
#             smallest = set(nums1)
#             largest = set(nums2)
#         else:
#             smallest = set(nums2)
#             largest = set(nums1)

#         for val in smallest:
#             if (val in largest):
#                 intersect.append(val)
#         return intersect
