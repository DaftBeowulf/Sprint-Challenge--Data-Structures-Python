import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# O(n) runtime, averages around .01-.02 seconds
names_hash = {}

for n in names_1 + names_2:
    if names_hash.get(n):
        duplicates.append(n)
    else:
        names_hash[n] = n

# stretch BST solution, O(n log n) runtime, averages .16 seconds


# class BinarySearchTree:
#     def __init__(self, name):
#         self.name = name
#         self.left = None
#         self.right = None

#     def insert(self, name):
#         # greater names alphabetically become right child
#         if self.name < name:
#             if self.right:
#                 self.right.insert(name)
#             else:
#                 self.right = BinarySearchTree(name)
#         # alphabetically lower names become left child
#         elif self.name > name:
#             if self.left:
#                 self.left.insert(name)
#             else:
#                 self.left = BinarySearchTree(name)
#         else:  # names are equal--a duplicate
#             duplicates.append(name)


# bst = BinarySearchTree(names_1[0])

# for name in names_1[1:]+names_2:
#     bst.insert(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
