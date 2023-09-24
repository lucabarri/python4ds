class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert_children(self, other_node):
        if other_node.value <= self.value:
            self.left = other_node
        else:
            self.right = other_node


class Tree():
    def __init__(self):
        self.root = None

    def insert_node(self, node):
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            finished = False
            while not finished:
                if current_node.value <= node.value:
                    # In this case, go to the right
                    if current_node.right is None:
                        # We found where to put the new
                        # node
                        current_node.insert_children(node)
                        finished = True
                    else:
                        # We need to continue searching
                        # to the right.
                        current_node = current_node.right
                else:
                    # In this case, we go to the left
                    if current_node.left is None:
                        # We found where to put the new
                        # node
                        current_node.insert_children(node)
                        finished = True
                    else:
                        current_node = current_node.left

    def recursive_insert_node(self, node):
        if self.root is None:
            self.root = node
            return
        else:
            pass

    def search(self, x):
        # Initialization: we start iteration at the root.
        current_node = self.root
        # Finished will be our flag. We loop untill it is
        # True.
        finished = False

        while not finished:
            if current_node.value < x:
                # In this case, we need to look to the right.
                if current_node.right is None:
                    # In this case... Too bad, the value
                    # is not in the tree.
                    current_node = None
                    finished = True
                else:
                    current_node = current_node.right
            elif current_node.value > x:
                # In this case, we need to look to the left.
                if current_node.left is None:
                    # In this case... Too bad, the value
                    # is not in the tree.
                    current_node = None
                    finished = True
                else:
                    current_node = current_node.left
            else:
                finished = True
        return current_node

    def print(self, node, message):
        message = f"{node.value} ("
        if node.left is not None:
            message += f"left: {node.left.value}, "
        else:
            message += "left: None, "

        if node.right is not None:
            message += f"right: {node.right.value})\n"
        else:
            message += "right: None)\n"

        if node.left is not None:
            message += self.print(node.left, message)
        if node.right is not None:
            message += self.print(node.right, message)

        return message

    def __str__(self):
        return self.print(node=self.root, message='')


t = Tree()
r = Node(8)
t.insert_node(r)
new_node = Node(3)
t.insert_node(new_node)
new_node = Node(10)
t.insert_node(new_node)
new_node = Node(1)
t.insert_node(new_node)
new_node = Node(7)
t.insert_node(new_node)
new_node = Node(9)
t.insert_node(new_node)
new_node = Node(14)
t.insert_node(new_node)
