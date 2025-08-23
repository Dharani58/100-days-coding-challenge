class Solution:
    def mergeTwoLists(self, list1, list2):
        res=[]
        while list1:
            res.append(list1.val)
            list1=list1.next
        while list2:
            res.append(list2.val)
            list2=list2.next
        res.sort()
        start=None
        head=None
        for i in res:
            if start==None:
                start=ListNode(i)
                head=start
            else:
                n=ListNode(i)
                start.next=n
                start=n
        return head