import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

# BST pseudocode:
"""
for n in names_1+names_2: # O(n) runtime
    BST.insert(n) # creates BST filled with names, can be sorted alphabetically
    BUT insert appends it to the duplicate array instead if strictly equal (dupe)
    so BST.insert for the whole concatenated array would approach O(log n)
"""

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
