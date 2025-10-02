
from __future__ import annotations
from typing import List, Tuple
import heapq

def connect_cables(lengths: List[int]) -> Tuple[int, List[Tuple[int,int,int]]]:
    """
    Given cable lengths, repeatedly connect the two shortest.
    Cost of each connection = sum of the two lengths.
    Return (total_cost, merges), where merges is a list of (a,b,cost) for each step.
    If 0 or 1 cables are given, cost is 0 and merges is empty.

    This is identical to the optimal greedy strategy used in Huffman coding.
    Time: O(n log n), Space: O(n).
    """
    if not lengths or len(lengths) == 1:
        return 0, []

    heap = list(lengths)
    heapq.heapify(heap)
    total = 0
    merges: List[Tuple[int,int,int]] = []

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost = a + b
        total += cost
        merges.append((a, b, cost))
        heapq.heappush(heap, cost)

    return total, merges


# Self-test
if __name__ == "__main__":
    total, merges = connect_cables([8, 4, 6, 12])
    # Optimal order: (4+6)=10, (8+10)=18, (12+18)=30 => total 10+18+30=58
    assert total == 58
    print("cables.py self-test passed")