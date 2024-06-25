from .models import Post
import dhash

class BKTreeNode:
    def __init__(self, hash_value, post_id):
        self.hash_value = hash_value
        self.post_id = post_id
        self.children = {}

class BKTree:
    def __init__(self):
        self.root = None

    def insert(self, hash_value, post_id):
        new_node = BKTreeNode(hash_value, post_id)
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while True:
            distance = dhash.get_num_bits_different(int(current_node.hash_value, 16), int(hash_value, 16))
            if distance not in current_node.children:
                current_node.children[distance] = new_node
                break
            else:
                current_node = current_node.children[distance]

    def query(self, hash_value, tolerance):
        if self.root is None:
            return []

        result = []
        nodes_to_check = [self.root]
        
        while nodes_to_check:
            current_node = nodes_to_check.pop()
            distance = dhash.get_num_bits_different(int(current_node.hash_value, 16), int(hash_value, 16))
            if distance <= tolerance:
                result.append((current_node.post_id, distance))
            
            for d in range(max(0, distance - tolerance), distance + tolerance + 1):
                if d in current_node.children:
                    nodes_to_check.append(current_node.children[d])
        
        return result

def build_bktree():
    tree = BKTree()
    for post in Post.objects.all():
        if post.image_hash:
            tree.insert(post.image_hash, post.id)
    return tree

bktree = build_bktree()