import matplotlib.pyplot as plt
import networkx as nx
import colorsys
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def build_tree_from_list(values):
    """Build a binary tree from a list of values (level by level)"""
    if not values:
        return None
    
    root = Node(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Add left child
        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        
        # Add right child
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
    
    return root

def generate_colors(steps):
    """Generate a color gradient from dark to light shades"""
    colors = []
    for i in range(steps):
        # Use HSV color model for better control
        hue = 0.6  # Blue hue
        saturation = 0.8
        value = 0.3 + 0.6 * (i / (steps - 1) if steps > 1 else 0.5)  # Dark to light
        
        r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
        hex_color = f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'
        colors.append(hex_color)
    
    return colors

def build_graph(root):
    """Convert binary tree to NetworkX graph for visualization"""
    G = nx.DiGraph()
    pos = {}
    node_to_id = {}
    
    # Build the graph using BFS
    queue = deque([(root, '0', 0, 0)])  # (node, id, x, y)
    while queue:
        node, node_id, x, y = queue.popleft()
        if node:
            G.add_node(node_id, value=node.val)
            pos[node_id] = (x, -y)  # Negative y to put root at top
            node_to_id[node] = node_id
            
            if node.left:
                left_id = f"{node_id}L"
                G.add_edge(node_id, left_id)
                queue.append((node.left, left_id, x-1/(2**(y)), y+1))
            
            if node.right:
                right_id = f"{node_id}R"
                G.add_edge(node_id, right_id)
                queue.append((node.right, right_id, x+1/(2**(y)), y+1))
    
    return G, pos, node_to_id

def dfs_traversal(root):
    """Perform DFS traversal using a stack (not recursion)"""
    if not root:
        return []
    
    visited = []
    stack = [root]
    
    while stack:
        current = stack.pop()
        visited.append(current)
        
        # Push right first so left is processed first (LIFO)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return visited

def bfs_traversal(root):
    """Perform BFS traversal using a queue"""
    if not root:
        return []
    
    visited = []
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        visited.append(current)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return visited

def visualize_traversal(root, traversal_type):
    """Visualize tree traversal with colored nodes"""
    if not root:
        return []
    
    # Build the graph
    G, pos, node_to_id = build_graph(root)
    
    # Perform traversal
    if traversal_type == 'DFS':
        visited_nodes = dfs_traversal(root)
        title = "Depth-First Search (DFS) Traversal"
    else:  # BFS
        visited_nodes = bfs_traversal(root)
        title = "Breadth-First Search (BFS) Traversal"
    
    # Generate colors based on traversal order
    colors = generate_colors(len(visited_nodes))
    node_colors = {node_to_id[visited_nodes[i]]: colors[i] for i in range(len(visited_nodes))}
    
    # Create the visualization
    plt.figure(figsize=(12, 8))
    nx.draw(
        G, pos, 
        with_labels=False, 
        node_color=[node_colors.get(n, '#CCCCCC') for n in G.nodes()],
        node_size=700
    )
    
    # Add value labels to nodes
    labels = {node_id: G.nodes[node_id]['value'] for node_id in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels)
    
    plt.title(title)
    plt.axis('off')
    filename = f"{traversal_type.lower()}_traversal.png"
    plt.savefig(filename)
    plt.show()
    
    # Return values in traversal order for display
    return [node.val for node in visited_nodes]

if __name__ == "__main__":
    # Create a sample binary tree with 15 nodes
    tree_data = [i for i in range(1, 16)]  # Values 1 to 15
    root = build_tree_from_list(tree_data)
    
    # Visualize DFS traversal
    dfs_result = visualize_traversal(root, 'DFS')
    print("DFS traversal order:", dfs_result)
    
    # Visualize BFS traversal
    bfs_result = visualize_traversal(root, 'BFS')
    print("BFS traversal order:", bfs_result)
