
import unittest
from trees import BST, AVL, find_min, sum_tree
from cables import connect_cables

class TestHW08(unittest.TestCase):
    def test_task1_min_bst(self):
        bst = BST([10,5,1,7,40,50])
        self.assertEqual(find_min(bst.root), 1)

    def test_task1_min_avl(self):
        avl = AVL([10,20,30,40,50,25])
        self.assertEqual(find_min(avl.root), 10)

    def test_task2_sum(self):
        bst = BST([2,1,3])
        self.assertEqual(sum_tree(bst.root), 6)

    def test_task3_cables(self):
        total, merges = connect_cables([8,4,6,12])
        self.assertEqual(total, 58)
        self.assertEqual(len(merges), 3)  # n-1 merges

    def test_edge_cases(self):
        self.assertEqual(connect_cables([])[0], 0)
        self.assertEqual(connect_cables([5])[0], 0)
        self.assertIsNone(find_min(None))
        self.assertEqual(sum_tree(None), 0)

if __name__ == "__main__":
    unittest.main()