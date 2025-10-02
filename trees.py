
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterable, Tuple, List

@dataclass
class Node:
    """Basic tree node used for both BST and AVL trees."""
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    height: int = 1  # used by AVL; harmless for plain BST

    def __iter__(self):
        """In-order traversal (yields sorted keys for BST/AVL)."""
        if self.left:
            yield from self.left
        yield self.key
        if self.right:
            yield from self.right


# ---------------------------
# Binary Search Tree (BST)
# ---------------------------

class BST:
    def __init__(self, keys: Optional[Iterable[int]] = None):
        self.root: Optional[Node] = None
        if keys:
            for k in keys:
                self.insert(k)

    def insert(self, key: int) -> None:
        """Insert key into BST (iterative)."""
        if self.root is None:
            self.root = Node(key)
            return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left is None:
                    cur.left = Node(key)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(key)
                    return
                cur = cur.right

    def __iter__(self):
        return iter(self.root) if self.root else iter(())


# ---------------------------
# AVL Tree (self-balancing)
# ---------------------------

def _height(n: Optional[Node]) -> int:
    return n.height if n else 0

def _update(n: Node) -> None:
    n.height = 1 + max(_height(n.left), _height(n.right))

def _balance_factor(n: Node) -> int:
    return _height(n.left) - _height(n.right)

def _rotate_right(y: Node) -> Node:
    x = y.left
    assert x is not None
    T2 = x.right
    x.right = y
    y.left = T2
    _update(y)
    _update(x)
    return x

def _rotate_left(x: Node) -> Node:
    y = x.right
    assert y is not None
    T2 = y.left
    y.left = x
    x.right = T2
    _update(x)
    _update(y)
    return y

class AVL:
    def __init__(self, keys: Optional[Iterable[int]] = None):
        self.root: Optional[Node] = None
        if keys:
            for k in keys:
                self.insert(k)

    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)

    def _insert(self, node: Optional[Node], key: int) -> Node:
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        _update(node)
        bf = _balance_factor(node)

        # Left heavy
        if bf > 1:
            if key > node.left.key:  # Left-Right
                node.left = _rotate_left(node.left)
            return _rotate_right(node)
        # Right heavy
        if bf < -1:
            if key < node.right.key:  # Right-Left
                node.right = _rotate_right(node.right)
            return _rotate_left(node)

        return node

    def __iter__(self):
        return iter(self.root) if self.root else iter(())


# ---------------------------
# Generic tree algorithms
# ---------------------------

def find_min(root: Optional[Node]) -> Optional[int]:
    """
    Find the minimum key in a BST/AVL.
    Works for any BST-like tree where the smallest is the left-most node.
    Returns None for empty tree.
    """
    cur = root
    if cur is None:
        return None
    while cur.left:
        cur = cur.left
    return cur.key


def sum_tree(root: Optional[Node]) -> int:
    """Sum of all keys in the tree. Handles empty trees."""
    if root is None:
        return 0
    # Tail-recursive style using stack to avoid recursion limit
    s = 0
    stack: List[Optional[Node]] = [root]
    while stack:
        n = stack.pop()
        if n is None:
            continue
        s += n.key
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)
    return s


# Small self-test
if __name__ == "__main__":
    bst = BST([10, 5, 1, 7, 40, 50])
    avl = AVL([10, 20, 30, 40, 50, 25])

    assert find_min(bst.root) == 1
    assert sum_tree(bst.root) == sum([10, 5, 1, 7, 40, 50])

    assert find_min(avl.root) == 10
    assert sum_tree(avl.root) == sum([10, 20, 30, 40, 50, 25])
    print("trees.py self-test passed")