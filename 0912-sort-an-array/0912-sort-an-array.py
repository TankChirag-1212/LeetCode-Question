class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) > 1:
                left = nums[:len(nums)//2]
                right = nums[len(nums)//2:]
                
                
                mergeSort(left)
                mergeSort(right)
                
                i,j,k = 0, 0, 0
                
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        nums[k] = left[i]
                        i += 1
                    else:
                        nums[k] = right[j]
                        j += 1
                    k += 1
                while i < len(left):
                    nums[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right):
                    nums[k] = right[j]
                    j += 1
                    k += 1
            return nums
        return mergeSort(nums)
    
# there are so many sorting algo which can be used to sort arr in nlogn like merge sort, heap sort, binary tree, etc...but we use merge sort here.
# in merge sort we use the Divide and Conquer method.
# first we divide the arr into half and we continue until there is only on element left in the arr.
# then we compare the elements in all arr and merge them into the new temp arr in the acending order.
# to do so we use the 3 pts i,j,k...i for the splited left arr, j for the right spilited arr and k for the nums.
# we does not create the new arr in this case we just update the nums given to us from the start.
# time complexity is O(nlogn)....where n means n number of elements at every level in the tree and logn is the height of the tree.
# Space complexity is O(n) where n is the length of the nums.
