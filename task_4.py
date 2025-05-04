import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store the color of the nodede
        self.id = str(uuid.uuid4())  # Unique identifier for each node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Use id and store the node's value
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Use the node's value for labels

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# New function to build a tree from a binary heap
def build_heap_tree(heap_array):
    """
    Builds a binary tree from an array representing a binary heapeap
    """
    if not heap_array:
        return None

    # Create nodes for each element of the heap
    nodes = [Node(val) for val in heap_array]

    # Connect nodes according to the binary heap structure
    for i in range(len(nodes)):
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2

        if left_child_idx < len(nodes):
            nodes[i].left = nodes[left_child_idx]

        if right_child_idx < len(nodes):
            nodes[i].right = nodes[right_child_idx]

    # Return the root of the treeree
    return nodes[0]


def visualize_heap(heap_array):
    """
    Visualizes a binary heap represented as an array
    """
    if not heap_array:
        print("Empty heap")
        return

    # Build a tree from the heapheap
    root = build_heap_tree(heap_array)

    # Visualize the tree
    draw_tree(root)


def heapify(arr, n, i):
    """
    Converts the subtree rooted at i into a heapeap
    """
    largest = i  # Initialize the largest element as the root
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if the left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if the right child exists and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the root root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap elements
        heapify(arr, n, largest)


def build_max_heap(arr):
    """
    Builds a max-heap from an arrayan array
    """
    arr = arr.copy()  # Create a copy to avoid modifying the originalnal
    n = len(arr)

    # Build the heap (rearrange the array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    return arr


# Example usage
if __name__ == "__main__":
    # Create a test array
    arr = [3, 9, 2, 1, 4, 5]
    print("Original array:", arr)

    # Build a max-heap
    max_heap = build_max_heap(arr)
    print("Max-heap:", max_heap)

    # Visualize the max-heapp
    print("Max-heap visualization:")
    visualize_heap(max_heap)

    # Example with a binary heap from an imageage
    example_heap = [0, 4, 1, 5, 10, 3]
    print("\nExample heap from an image:")
    print(example_heap)
    print("Visualization of the example:")
    visualize_heap(example_heap)
