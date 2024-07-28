class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]
    
    # Depth-first search (DFS) to find the node with the given ID in the tree.
    while nodes_to_visit:
      node = nodes_to_visit.pop(0)
      if id == node.get('id'):
        return node
      nodes_to_visit = node['children'] + nodes_to_visit
      
    return None

    # Breadth-first search (BFS) to find the node with the given ID in the tree.
    while nodes_to_visit:
      node = nodes_to_visit.pop(0)
      if id == node.get('id'):
        return node
      nodes_to_visit += node['children']
      
    return None