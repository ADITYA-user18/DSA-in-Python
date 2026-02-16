class UnionOfArray:
    def ArrayUnion(self,nums1,nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        seen = []


        for i in range(0,n1):
            if nums1[i] not in seen:
                seen.append(nums1[i])
        
        for i in range(0,n2):
            if nums2[i] not in seen:
                seen.append(nums2[i])

       
        return seen
    
a =  UnionOfArray()
b = a.ArrayUnion([99,1,2,3,4,5,2,4,1,3,22,45],[4,7,8,5,9,44,1,6,2,55,32,12])
print(b)