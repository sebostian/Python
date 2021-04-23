'''
finds median of two sorted arrays
'''
def findMedianSortedArrays(self, nums1, nums2) -> float:
    c = merge(nums1, len(nums1), nums2, len(nums2))
    if len(c) % 2 == 1:
        median = c[len(c) // 2]
    else:
        j = len(c) // 2        
        median = (c[j] + c[j-1]) / 2     

    return median

'''
merges two sorted arrays
result is new sorted array
'''
def merge(nums1, m, nums2, n):
    i = 0
    j = 0
    c = []

    while (i < m or j < n):
        if (i == m):
            c.append(nums2[j])
            j += 1
            continue

        if (j == n):
            c.append(nums1[i])
            i += 1
            continue

        if (nums1[i] < nums2[j]):
            c.append(nums1[i])
            i += 1
        else:
            c.append(nums2[j])
            j += 1

    return c

a = [0,9,10]
b = [1,3]

m = findMedianSortedArrays(1, a, b)
print(m)


