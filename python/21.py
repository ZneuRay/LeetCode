# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
      if not list2:
        return None
      return list2
    if not list2:
      return list1
    head = None
    if list1.val <= list2.val:
      head = ListNode(list1.val)
      list1 = list1.next
    elif list1.val > list2.val:
      head = ListNode(list2.val)
      list2 = list2.next
    list = head
    while 1:
      if not list1:
        if not list2:
          return head
        l = ListNode(list2.val)
        list.next = l
        list = l
        list2 = list2.next
      if not list2:
        if not list1:
          return head
        l = ListNode(list1.val)
        list.next = l
        list = l
        list1 = list1.next

      if list1.val <= list2.val:
        l = ListNode(list1.val)
        list.next = l
        list = l
        list1 = list1.next
      elif list1.val > list2.val:
        l = ListNode(list2.val)
        list.next = l
        list = l
        list2 = list2.next
