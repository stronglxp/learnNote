#### 剑指 Offer 04. 二维数组中的查找

链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/

标签：**数组、双指针、二分**

> 题目

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

```java
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定 target = 5，返回 true。

给定 target = 20，返回 false。
    
0 <= n <= 1000

0 <= m <= 1000
```

> 分析

题目给定了一个二维数组，该数组的特点是每一行从左往右递增，每一列从上往下递增，并且要你设计一个高效的函数。那本意肯定不是让你直接二重循环去查找。

解法一：这时候就应该想到是用二分法去解决这道题目。我的思路是，循环列，对于每一行，先判断该数是否在该行的范围内，如果在，那么再使用二分查找在该行内查找这个数，查到了就返回，没查到就继续下一行。

解法二：仔细观察二维数组，可以发现，左下角和右上角连起来的对角线，把整个二维数组分成了两份，左上角的三角形是小于对角线的，右下角的三角形是大于对角线的。基于此，可以从右上角的数开始，遍历，如果target大于当前的数，则col--往左移动一列；如果target小于当前的数，则row++往下移动一行。

> 编码

**解法一**：

```java
class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        int m = matrix.length;
        for (int i = 0; i < m; i++) {
            int n = matrix[i].length;
            if (n <= 0 || target < matrix[i][0] || target > matrix[i][n - 1]) {
                continue;
            }

            int left = 0, right = n - 1;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (matrix[i][mid] == target) {
                    return true;
                } else if (matrix[i][mid] < target) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return false;
    }
}
```

![image-20210523163500094](剑指Offer04.二维数组中的查找.assets/image-20210523163500094.png)

时间复杂度O(mlogn)，空间复杂度O(1)

**解法2**：

```java
class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int m = 0, n = matrix[0].length - 1;
        while (m < matrix.length && n >= 0) {
            if (target > matrix[m][n]) {
                m++;
            } else if (target < matrix[m][n]) {
                n--;
            } else {
                return true;
            }
        }

        return false;
    }
}
```

![image-20210523165441302](剑指Offer04.二维数组中的查找.assets/image-20210523165441302.png)

时间复杂度O(m + n)，空间复杂度O(1)