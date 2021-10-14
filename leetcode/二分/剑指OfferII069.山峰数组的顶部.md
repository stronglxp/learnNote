#### 剑指 Offer II 069. 山峰数组的顶部

#### 2021-10-14 LeetCode每日一题

链接：https://leetcode-cn.com/problems/B1IidL/

标签：**数组、二分查找**

> 题目

符合下列属性的数组 arr 称为 山峰数组（山脉数组） ：

- arr.length >= 3
- 存在 i（0 < i < arr.length - 1）使得：
  - arr[0] < arr[1] < ... arr[i-1] < arr[i]
  - arr[i] > arr[i+1] > ... > arr[arr.length - 1]

给定由整数组成的山峰数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i ，即山峰顶部。

示例 1：

```java
输入：arr = [0,1,0]
输出：1
```

示例 2：

```java
输入：arr = [1,3,5,4,2]
输出：2
```

示例 3：

```java
输入：arr = [0,10,5,2]
输出：1
```

示例 4：

```java
输入：arr = [3,4,5,1]
输出：2
```

示例 5：

```java
输入：arr = [24,69,100,99,79,78,67,36,26,19]
输出：2
```


提示：

- 3 <= arr.length <= 10 ^ 4
- 0 <= arr[i] <= 10 ^ 6
- 题目数据保证 arr 是一个山脉数组


进阶：很容易想到时间复杂度 O(n) 的解决方案，你可以设计一个 O(log(n)) 的解决方案吗？

> 分析

解法1：循环。复杂度O(n)。

解法2：二分查找。因为峰顶的左边是一个升序数组，右边是一个降序数组，所以可以判断峰值是处于左边还是右边。复杂度O(logn)

> 编码

解法1：

```java
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        for (int i = 1; i < arr.length - 1; i++) {
            if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
                return i;
            }
        }

        return -1;
    }
}
```

![image-20211014201133801](剑指OfferII069.山峰数组的顶部.assets/image-20211014201133801.png)

解法2：

```java
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1]) {
                return mid;
            } else if (arr[mid] > arr[mid - 1] && arr[mid] < arr[mid + 1]) {
                // 峰值在右边
                left = mid;
            } else if (arr[mid] < arr[mid - 1] && arr[mid] > arr[mid + 1]) {
                // 峰值在左边
                right = mid;
            }
        }

        return -1;
    }
}
```

![image-20211014211409460](剑指OfferII069.山峰数组的顶部.assets/image-20211014211409460.png)