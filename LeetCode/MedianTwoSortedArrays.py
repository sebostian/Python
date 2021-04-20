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

    nums1.clear()
    for a in c:
        nums1.append(a)




a = [2, 100]
b = [2, 5, 7, 90]

merge(a, 2, b, 4)
print(a)

