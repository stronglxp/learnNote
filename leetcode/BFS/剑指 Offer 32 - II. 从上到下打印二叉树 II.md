#### 剑指 Offer 32 - II. 从上到下打印二叉树 II

链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/

```java
public class Test_32_2 {
    public List<List<Integer>> levelOrder(TreeNode1 root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }

        Queue<TreeNode1> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int len = queue.size();
            List<Integer> level = new ArrayList<>();

            // 每一层
            for (int i = 0; i < len; i++) {
                TreeNode1 node = queue.poll();
                level.add(node.val);
                if (node.left != null) {
                    queue.offer(node.left);
                }

                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            res.add(level);
        }

        return res;
    }
}

class TreeNode1 {
    int val;
    TreeNode1 left;
    TreeNode1 right;
    TreeNode1(int x) { val = x; }
}
```

