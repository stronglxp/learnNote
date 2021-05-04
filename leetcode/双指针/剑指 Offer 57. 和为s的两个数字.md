#### 剑指 Offer 57. 和为s的两个数字

链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/

```java
/**
 * 和为s的两个数字：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
 * 输入的是有序数组，看到有序数组，就应该想到双指针，这里使用左右指针
 */
public class Test_57 {
    public int[] twoSum(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum == target) {
                return new int[]{nums[left], nums[right]};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }

        // []
        return new int[0];
    }
}
```

