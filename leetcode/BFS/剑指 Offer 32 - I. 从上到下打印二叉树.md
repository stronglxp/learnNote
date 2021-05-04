#### 剑指 Offer 32 - I. 从上到下打印二叉树

链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/

```java
/**
 * 从上到下打印二叉树
 * @link https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/
 * BFS
 */
public class Test_32_1 {

    public int[] levelOrder(TreeNode root) {
        if (root == null) {
            return new int[0];
        }

        Queue<TreeNode> list = new LinkedList<>();
        List<Integer> res = new ArrayList<>();
        list.offer(root);

        while (!list.isEmpty()) {
            int len = list.size();
            for (int i = 0; i < len; i++) {
                TreeNode node = list.poll();
                res.add(node.val);
                if (node.left != null) {
                    list.offer(node.left);
                }

                if (node.right != null) {
                    list.offer(node.right);
                }
            }
        }

        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}
```

