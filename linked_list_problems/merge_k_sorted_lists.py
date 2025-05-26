import heapq
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # For heapq, we need to compare ListNodes.
    # If values are equal, Python's heapq might try to compare the ListNode objects themselves,
    # which can lead to errors if they are not comparable.
    # Adding a unique id or overriding __lt__ ensures stable sorting in the heap.
    # For this problem, standard library heapq handles tuples like (val, id, node) well.
    # We will store (node.val, unique_id, node) in the heap.
    # A simpler __lt__ can be defined if we only store nodes, but that can be tricky
    # if two nodes from different lists have the same value.
    def __lt__(self, other):
        # This makes ListNode comparable by value, which is needed for heapq
        # if we store nodes directly and there are value ties.
        # However, the (value, id, node) tuple strategy is generally more robust for heaps.
        return self.val < other.val

# Helper function to create a linked list from a Python list
def list_to_linked_list(elements: List[int]) -> Optional[ListNode]:
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for val in elements[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a Python list
def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    if not node:
        return []
    elements = []
    current = node
    while current:
        elements.append(current.val)
        current = current.next
    return elements

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists into one sorted linked list.

        Args:
            lists: A list of k ListNode heads, each representing a sorted linked list.

        Returns:
            The head of the merged sorted linked list.

        Approach: Min-Heap
        1. Initialize a min-heap.
        2. Add the head node of each of the k lists to the heap.
           Since ListNode objects themselves might not be directly comparable in all Python versions
           or configurations if values are equal (especially if not defining __lt__ or using Python < 3),
           it's common to store tuples like (value, unique_id, node) in the heap.
           The unique_id is used as a tie-breaker if values are the same, ensuring heap stability.
           A simple counter can provide this unique_id.
        3. While the heap is not empty:
           a. Extract the node with the smallest value from the heap. This node will be (value, id, actual_node).
           b. Add this `actual_node` to the result list.
           c. If `actual_node` has a `next` node, add `(actual_node.next.val, new_id, actual_node.next)` to the heap.
        4. Maintain a dummy head for the result list to simplify appending the first node.
        """
        if not lists:
            return None

        # Min-heap will store tuples: (node_value, unique_id, node_object)
        # unique_id is for tie-breaking if values are equal, ensuring heap can compare elements.
        min_heap = []
        unique_id_counter = 0  # To ensure unique items in heap for tie-breaking

        for head_node in lists:
            if head_node:
                heapq.heappush(min_heap, (head_node.val, unique_id_counter, head_node))
                unique_id_counter += 1

        # Dummy head for the merged list
        dummy_head = ListNode(-1)
        current_merged_list_node = dummy_head

        while min_heap:
            val, _, node = heapq.heappop(min_heap) # Pop the smallest node

            # Append this node to our merged list
            current_merged_list_node.next = node
            current_merged_list_node = current_merged_list_node.next

            # If there's a next node in the list from which 'node' came, add it to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, unique_id_counter, node.next))
                unique_id_counter += 1
        
        return dummy_head.next

if __name__ == "__main__":
    solver = Solution()

    # Helper for printing results
    def print_test_case(lists_of_lists, expected_list):
        input_linked_lists = [list_to_linked_list(l) for l in lists_of_lists]
        
        # Make copies for the function to consume if it modifies list structure internally
        # (though mergeKLists here only modifies .next pointers of nodes it puts in new list)
        input_linked_lists_for_func = [list_to_linked_list(l) for l in lists_of_lists]
        
        merged_head = solver.mergeKLists(input_linked_lists_for_func)
        result_list = linked_list_to_list(merged_head)
        
        input_repr = [[node.val for node in linked_list_to_list(ll_head)] for ll_head in input_linked_lists] # This is wrong, should be lists_of_lists
        
        print(f"Input lists: {lists_of_lists}")
        print(f"Merged list: {result_list}")
        print(f"Expected list: {expected_list}")
        print(f"Test Passed: {result_list == expected_list}\n")


    # Example 1
    lists1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
    expected1 = [1, 1, 2, 3, 4, 4, 5, 6]
    print_test_case(lists1, expected1)

    # Example 2: Empty list of lists
    lists2 = []
    expected2 = []
    print_test_case(lists2, expected2)

    # Example 3: List of lists containing some empty lists
    lists3 = [[], [1]]
    expected3 = [1]
    print_test_case(lists3, expected3)

    lists3b = [[1,3], [], [2,4]]
    expected3b = [1,2,3,4]
    print_test_case(lists3b, expected3b)

    # Example 4: List of lists where all are empty
    lists4 = [[], [], []]
    expected4 = []
    print_test_case(lists4, expected4)

    # Example 5: Lists with single elements
    lists5 = [[10], [1], [100]]
    expected5 = [1, 10, 100]
    print_test_case(lists5, expected5)

    lists5b = [[5]]
    expected5b = [5]
    print_test_case(lists5b, expected5b)

    # Example 6: Lists with varying lengths
    lists6 = [[1, 2, 3, 10, 20], [4, 5], [6, 7, 8]]
    expected6 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 20]
    print_test_case(lists6, expected6)

    # Example 7: One list is significantly longer
    lists7 = [[1,1,1,1,100], [2,3,4]]
    expected7 = [1,1,1,1,2,3,4,100]
    print_test_case(lists7, expected7)
```
