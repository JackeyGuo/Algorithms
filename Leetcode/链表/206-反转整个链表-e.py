# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        反转整个单链表
        """
        # base case, 当前节点没有 next 节点，直接返回
        if head == None or head.next == None: return head

        last = self.reverseList(head.next)

        # 反转，使得当前节点的 next 节点的 next 指向自己
        head.next.next = head
        # 当链表递归反转之后，新的头节点是last，而之前的head变成了最后一个节点，别忘了链表的末尾要指向 null
        head.next = None

        return last
