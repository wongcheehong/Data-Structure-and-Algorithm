import json


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):  # sourcery skip: merge-else-if-into-elif
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return
        currentNode = self.root
        while True:
            if value < currentNode.value:  # Go left
                if currentNode.left is None:
                    currentNode.left = newNode
                    break
                currentNode = currentNode.left
            else:  # Go right
                if currentNode.right is None:
                    currentNode.right = newNode
                    break
                currentNode = currentNode.right

    def lookup(self, value):
        if self.root is None:
            return False

        currentNode = self.root
        while currentNode is not None:
            if value == currentNode.value:
                return True
            if value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return False

    def remove(self, value):  # sourcery skip: merge-else-if-into-elif
        if self.root is None:
            return None

        parentNode = None
        currentNode = self.root
        while currentNode:
            if value == currentNode.value:
                if currentNode.right is None:  # No right child
                    parentNode.left = currentNode.left
                elif currentNode.right.left is None:  # Right child that doesn't have left child
                    if parentNode.left is currentNode:
                        parentNode.left = currentNode.right
                    else:
                        parentNode.right = currentNode.right
                else:  # Right child that has left child
                    parentNodeOfLeftMostChild = currentNode.right
                    leftMostChild = currentNode.right.left
                    while leftMostChild.left:
                        parentNodeOfLeftMostChild = leftMostChild
                        leftMostChild = leftMostChild.left

                    # Parents left subtree is now leftmost's right subtree
                    parentNodeOfLeftMostChild.left = leftMostChild.right
                    leftMostChild.left = currentNode.left
                    leftMostChild.right = currentNode.right

                    # if parentNode is None means that removedNode is root
                    if parentNode is None:
                        self.root = leftMostChild
                    else:
                        if parentNode.left is currentNode:
                            parentNode.left = leftMostChild
                        else:
                            parentNode.right = leftMostChild

            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            else:
                parentNode = currentNode
                currentNode = currentNode.right
        return None

    def breadthFirstSearch(self):
        currentNode = self.root
        node_list = []
        queue = [currentNode]

        while queue:
            currentNode = queue.pop(0)
            node_list.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        return node_list

    def breadthFirstSearchR(self, queue, node_list):
        if not queue:
            return node_list

        currentNode = queue.pop(0)
        node_list.append(currentNode.value)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

        return self.breadthFirstSearchR(queue, node_list)


def traverse(node):
    tree = {"value": node.value}
    tree["left"] = None if node.left is None else traverse(node.left)
    tree["right"] = None if node.right is None else traverse(node.right)
    with open("tree.json", "w") as f:
        json.dump(tree, f)
    return tree


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

print(tree.breadthFirstSearch())
# print(tree.breadthFirstSearchR([tree.root], []))
