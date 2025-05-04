class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)
    
    def reverse(self):
        previous = None
        current = self.head
        
        while current:
            next_node = current.next  
            current.next = previous  
            previous = current        
            current = next_node       
            
        self.head = previous 
    
    def sort(self):
        self.head = self._merge_sort(self.head)
        
    def _merge_sort(self, head):
        """Helper function for merge sort"""
        # Base case
        if not head or not head.next:
            return head
            
        # Get the middle of the list
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        
        # Apply merge sort recursively
        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)
        
        # Merge the sorted halves
        sorted_list = self._sorted_merge(left, right)
        return sorted_list
        
    def _get_middle(self, head):
        """Helper function to find the middle node"""
        if not head:
            return head
            
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
    def _sorted_merge(self, a, b):
        """Merge two sorted linked lists"""
        result = None
        
        # Base cases
        if not a:
            return b
        if not b:
            return a
            
        # Pick either a or b and recur
        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
            
        return result

def merge_sorted_lists(list1, list2):
    """Merge two sorted linked lists into one sorted list"""
    # Create a new linked list for the result
    merged_list = LinkedList()
    
    # Handle empty lists
    if not list1.head:
        return list2
    if not list2.head:
        return list1
        
    # Use the _sorted_merge helper to merge the heads
    helper = LinkedList()  # Create temporary instance just to use the method
    merged_list.head = helper._sorted_merge(list1.head, list2.head)
    
    return merged_list

def main():
    print("Example 1: Reversing a linked list")
    llist1 = LinkedList()
    for i in range(1, 6):
        llist1.insert_at_end(i)
    print(f"Original list: {llist1.display()}")
    llist1.reverse()
    print(f"Reversed list: {llist1.display()}")
    print()
    
    print("Example 2: Sorting a linked list")
    llist2 = LinkedList()
    llist2.insert_at_end(4)
    llist2.insert_at_end(2)
    llist2.insert_at_end(1)
    llist2.insert_at_end(3)
    llist2.insert_at_end(5)
    print(f"Unsorted list: {llist2.display()}")
    llist2.sort()
    print(f"Sorted list: {llist2.display()}")
    print()
    
    print("Example 3: Merging two sorted lists")
    llist3 = LinkedList()
    llist3.insert_at_end(1)
    llist3.insert_at_end(3)
    llist3.insert_at_end(5)
    
    llist4 = LinkedList()
    llist4.insert_at_end(2)
    llist4.insert_at_end(4)
    llist4.insert_at_end(6)
    
    print(f"First sorted list: {llist3.display()}")
    print(f"Second sorted list: {llist4.display()}")
    
    merged_list = merge_sorted_lists(llist3, llist4)
    print(f"Merged sorted list: {merged_list.display()}")
    
if __name__ == "__main__":
    main()
