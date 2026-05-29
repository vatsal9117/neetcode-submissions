"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # def __init__(self):
    #     self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldTocopy =  collections.defaultdict(lambda:Node(0))
        oldTocopy[None] = None

        cur = head
        while cur:
            oldTocopy[cur].val = cur.val
            oldTocopy[cur].next = oldTocopy[cur.next]
            oldTocopy[cur].random = oldTocopy[cur.random]
            cur = cur.next
        return oldTocopy[head]
