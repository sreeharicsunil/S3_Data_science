import numpy as np

nums1 = np.array([2,2,3,2,1])
nums2 = np.array([2,3,4,3,1])
print("Original Arrays\n", nums1, "\n", nums2)
print("\nTest said two arrays are equal\n", nums1 == nums2, "\n", np.equal(nums1,nums2))