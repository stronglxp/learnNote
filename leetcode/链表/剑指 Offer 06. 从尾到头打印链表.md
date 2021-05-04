#### 剑指 Offer 06. 从尾到头打印链表

链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/

```java
/**
 * @link https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
 */
public class Test_06 {
    public int[] reversePrint(ListNode head) {
//        Deque<Integer> res = new LinkedList<>();
//
//        while (head != null) {
//            res.offerFirst(head.val);
//            head = head.next;
//        }
//
//        return res.stream().mapToInt(Integer::intValue).toArray();
        ListNode node1 = head;
        int count = 0;
        while (node1 != null) {
            count++;
            node1 = node1.next;
        }

        int[] nums = new int[count];
        ListNode node2 = head;
        while (node2 != null) {
            nums[--count] =  node2.val;
            node2 = node2.next;
        }

        return nums;
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
```

