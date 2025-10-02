
from trees import BST, AVL, find_min, sum_tree
from cables import connect_cables

def demo():
    print("=== Task 1 & 2: Trees ===")
    bst = BST([10, 5, 1, 7, 40, 50])
    print("BST min:", find_min(bst.root))
    print("BST sum:", sum_tree(bst.root))

    avl = AVL([10, 20, 30, 40, 50, 25])
    print("AVL min:", find_min(avl.root))
    print("AVL sum:", sum_tree(avl.root))

    print("\n=== Task 3: Cables ===")
    lengths = [8, 4, 6, 12]
    total, merges = connect_cables(lengths)
    print("Lengths:", lengths)
    print("Total minimal cost:", total)
    print("Merge order (a, b, cost):", merges)

if __name__ == "__main__":
    demo()