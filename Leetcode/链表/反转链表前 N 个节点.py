# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.successor = None

    # 将链表的前 n 个节点反转（n <= 链表长度）
    def reverseN(self, head: ListNode, n: int) -> ListNode:
        """
        反转整个单链表
        """
        # base case 变为n == 1，反转一个元素，就是它本身，同时要记录后驱节点
        if n == 1:
            # 记录第 n + 1 个节点
            self.successor = head.next
            return head
        # 递归：N 逐渐 - 1， 以 head.next 为起点，需要反转前 n - 1 个节点
        last = self.reverseN(head.next, n - 1)

        # 反转，使得当前节点的 next 节点的 next 指向自己
        head.next.next = head
        # 让反转之后的 head 节点和后面的节点连起来
        head.next = self.successor

        return last
