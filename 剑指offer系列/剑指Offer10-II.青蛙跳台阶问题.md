#### 剑指 Offer 10- II. 青蛙跳台阶问题

链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/

标签：递归、动态规划

> 题目

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

```java
输入：n = 2
输出：2
    
输入：n = 7
输出：21
    
输入：n = 0
输出：1
```

**提示：**

- `0 <= n <= 100`

> 分析

这道本质上还是斐波那契数列，只是初始值不一样，斐波那契数列f(0) = 0, f(1) = 1，而这里f(0) = f(1) = 1。

定义dp[i]表示跳上一个i级台阶的跳法数，则dp[0] = dp[1] = 1，对于任意i（i >=2），跳上i级台阶可以通过跳1级或者跳2级到达，所以dp[i] = d[i - 1] + dp[i - 2]

对于本题，可以使用动态规划或者递归求解，使用递归需要保存计算过程中重复出现的项，减少运算时间。而使用动态规划，因为只和两个状态有关，所以空间复杂度可以由O(n)降为O(1)

> 编码

**递归版本**：

```java
class Solution {
    int[] cache = new int[101];
    public int numWays(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }

        if (cache[n] != 0) {
            return cache[n];
        }

        cache[n] = (numWays(n - 1) + numWays(n - 2)) % 1000000007;
        return cache[n];
    }
}
```

![image-20210618230418444](剑指Offer10-II.青蛙跳台阶问题.assets/image-20210618230418444.png)

**动态规划，空间复杂度O(n)**:

```java
class Solution {
    public int numWays(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }

        int[] dp = new int[n + 1];
        dp[0] = dp[1] = 1;

        for (int i = 2; i <= n; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007;
        }

        return dp[n];
    }
}
```

![image-20210618230241968](剑指Offer10-II.青蛙跳台阶问题.assets/image-20210618230241968.png)

**动态规划，空间复杂度O(1)**:

```java
class Solution {
    public int numWays(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }

        int res = 0, a1 = 1, a2 = 1;

        for (int i = 2; i <= n; i++) {
            res = a1 + a2;
            if (res >= 1000000007) {
                res = res % 1000000007;
            }
            a1 = a2;
            a2 = res;
        }

        return res;
    }
}
```

![image-20210618225752067](剑指Offer10-II.青蛙跳台阶问题.assets/image-20210618225752067.png)