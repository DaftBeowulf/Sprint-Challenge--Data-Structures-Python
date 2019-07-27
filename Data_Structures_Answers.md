Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
   O(1) -- adding an item to the specified index at self.current and incrementing or resetting self.current performs at the same runtime no matter the item passed in

2. What is the space complexity of your ring buffer's `append` function?
   O(n) -- it never needs to take up more values in the storage array than is passed in with the capacity

3. What is the runtime complexity of your ring buffer's `get` method?
   O(n) -- it never iterates over more items than the passed-in capacity

4) What is the space complexity of your ring buffer's `get` method?
   O(n) -- the result array grows according to the non-None values in storage, with a max of self.capacity

5) What is the runtime complexity of the provided code in `names.py`?
   O(n^2) -- must traverse each item in names_1 for each item in names_2

6) What is the space complexity of the provided code in `names.py`?
   O(n) -- the duplicates array grows averages to a linear growth according to the length of the names arrays

7) What is the runtime complexity of your optimized code in `names.py`?
   O(n log n) -- iterating over each name in the combined arrays is n, and the bst.insert method itself takes log n time

8) What is the space complexity of your optimized code in `names.py`?
   O(n) -- the binary search tree and duplicates array both grow linearly (on average) with the length of the names arrays
