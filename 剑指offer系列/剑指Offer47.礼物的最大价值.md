#### 剑指 Offer 47. 礼物的最大价值

#### 2023-03-08 LeetCode每日一题

链接：https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/

标签：**数组、动态规划、矩阵**

> 题目

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:

```java
输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
```


提示：

- 0 < grid.length <= 200
- 0 < grid[0].length <= 200

> 分析

对于每一个格子，每次只能往右或者往下移动一格。可以从左上角开始，记录下每个格子当前最多能拿到多少价值的礼物，最后右下角的值就是结果。

> 编码

```java
class Solution {
    public int maxValue(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dp = new int[m][n];
        dp[0][0] = grid[0][0];
        // 计算第一列
        for (int i = 1; i < m; i++) {
            dp[i][0] = grid[i][0] + dp[i - 1][0];
        }
        // 计算第一行
        for (int i = 1; i < n; i++) {
            dp[0][i] = grid[0][i] + dp[0][i - 1];
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = grid[i][j] + Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }

        return dp[m - 1][n - 1];
    }
}
```

![image-20230308215348332](剑指Offer47.礼物的最大价值.assets/image-20230308215348332-8283629.png)