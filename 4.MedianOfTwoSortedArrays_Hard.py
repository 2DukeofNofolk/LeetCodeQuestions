# 4. MEDIAN OF TWO SORTED ARRAYS (HARD)

import math

# nums1 = [1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# nums2 = [3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20]

nums1 = [2, 3, 4]
#
nums2 = [1, 2]


# CREATE FUNCTION HERE
# DEFINE BASE CASE FOR RECURSIVE CALL
def findMedianSortedArrays(nums1, nums2):

    # Finding the value in the list closest to the one given, will only work with less than the highest value in the list
    # Requires a value and a sorted List, the third parameter should also be the same sorted List as in the second parameter
    # MOVE TO BECOME HELPER FUNCTION
    def binaryInsert(insertValue, insertList, keepList):

        while len(insertList) > 1:
            mid = int(math.floor(len(insertList) / 2))
            if insertValue > insertList[mid]:
                insertList = insertList[mid:]
            elif insertValue < insertList[mid]:
                insertList = insertList[:mid]
            elif insertValue == insertList[mid]:
                return keepList.index(insertList[mid])

        insertIndexValue = keepList.index(insertList[0])

        if insertValue > keepList[insertIndexValue]:
            # CHANGE THIS!!!
            while (insertIndexValue + 1) < len(keepList) and keepList[insertIndexValue] == keepList[insertIndexValue + 1]:
                insertIndexValue += 1
            return insertIndexValue + 1
        else:
            return insertIndexValue
    

    def sortedArraysHelper(nums1, nums2, k, even):

        # Finding the position of the middle value of nums2
        mid = int(math.floor(len(nums2) / 2))

        # Check to see if the mid value is less than the last number in nums1 to see if can be inserted at all, if not,
        # then move to front half of nums2.

        pos = 0


        # INSERT BASE CASE
        # What if k is odd/even
        # Insert nums2[0] into nums1, then extract k
        if len(nums2) <= 1:
            if len(nums2) > 0:
                nums1.insert(binaryInsert(nums2[0], nums1, nums1), nums2[0])
            if even:
                return (nums1[k-1] + nums1[k]) / 2
            else:
                return nums1[k]

        # INSERT CHECK HERE
        if nums2[mid] <= nums1[-1]:
            # Storing the returning value
            pos = binaryInsert(nums2[mid], nums1, nums1)
        else:
            # Make recursive call with the front half of nums2
            return sortedArraysHelper(nums1, nums2[:mid], k, even)

        # If the length of nums1 up to where the value would be inserted plus the length of nums2 up to the value to
        # insert is greater than length k, then the other halves of either list cannot contain the median, so they can
        # be discarded.
        # The mid value of the front half of nums2 is then examined.
        if len(nums2[:mid + 1]) + len(nums1[:pos]) > k:
            nums2 = nums2[:mid]
            nums1 = nums1[:pos]
            # SET UP FOR RECURSIVE CALL
            # RECURSIVE CALL HERE
            return sortedArraysHelper(nums1, nums2, k, even)
        # If adding these lengths is less than k, then nums1 is kept the same length, the front of nums2 is inserted
        # into nums1 and the mid point of the back half of nums2 examined.
        elif len(nums2[:mid + 1]) + len(nums1[:pos]) <= k:
            nums1.insert(pos, nums2[mid])
            # for i in nums2[:mid]:
            for i in range(len(nums2[:mid-1]), -1, -1):
                nums1.insert(pos, nums2[i])
            nums2 = nums2[mid + 1:]
            # SET UP FOR RECURSIVE CALL
            # FOR THE RECURSIVE CALL YOU CAN ONLY SUBMIT TWO LISTS, SO YOU NEED TO INSERT THE FRONT HALF OF NUMS2 INTO
            # NUMS1
            # RECURSIVE CALL HERE
            return sortedArraysHelper(nums1, nums2, k, even)


    # Finding the kth position value
    t = len(nums1) + len(nums2)

    k = int(math.floor(t / 2))

    even = False

    if (len(nums1) + len(nums2)) % 2 == 0:
        even = True


    # If the length of nums1 is greater than k, then it can be safely cut down to length k without losing the median
    # value.
    if len(nums1) > k:
        nums1 = nums1[:k]
    

    # return sortedArraysHelper(nums1, nums2, k, even)

    if len(nums1) >= len(nums2):
        return sortedArraysHelper(nums1, nums2, k, even)
    else:
        return sortedArraysHelper(nums2, nums1, k, even)


print(findMedianSortedArrays(nums1, nums2))




