import sys

class Node:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1

    def getColor(self):
        if self.color == 0:
            return "Black"
        else:
            return "Red"


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0 # 0 = Black, 1 = Red
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def deleteAndBalance(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.rotateLeft(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.rotateRight(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.rotateLeft(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.rotateRight(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.rotateLeft(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.rotateRight(x.parent)
                    x = self.root
        x.color = 0

    def __transplant(self, a, b):
        if a.parent == None:
            self.root = b
        elif a == a.parent.left:
            a.parent.left = b
        else:
            a.parent.right = b
        b.parent = a.parent

    def delete(self, key):
        root = self.root
        z = self.TNULL
        while root != self.TNULL:
            if root.item == key:
                z = root

            if root.item <= key:
                root = root.right
            else:
                root = root.left

        if z == self.TNULL:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.deleteAndBalance(x)


    def insertAndBalance(self, inItem):
        while inItem.parent.color == 1:
            if inItem.parent == inItem.parent.parent.right:
                u = inItem.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    inItem.parent.color = 0
                    inItem.parent.parent.color = 1
                    inItem = inItem.parent.parent
                else:
                    if inItem == inItem.parent.left:
                        inItem = inItem.parent
                        self.rotateRight(inItem)
                    inItem.parent.color = 0
                    inItem.parent.parent.color = 1
                    self.rotateLeft(inItem.parent.parent)
            else:
                u = inItem.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    inItem.parent.color = 0
                    inItem.parent.parent.color = 1
                    inItem = inItem.parent.parent
                else:
                    if inItem == inItem.parent.right:
                        inItem = inItem.parent
                        self.rotateLeft(inItem)
                    inItem.parent.color = 0
                    inItem.parent.parent.color = 1
                    self.rotateRight(inItem.parent.parent)
            if inItem == self.root:
                break
        self.root.color = 0

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def rotateLeft(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotateRight(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.insertAndBalance(node)

    def searchTreeHelp(self, node, key):
        if node == self.TNULL or key == node.item:
            return node

        if key < node.item:
            return self.searchTreeHelp(node.left, key)
        return self.searchTreeHelp(node.right, key)

    def searchTree(self, key):
        return self.searchTreeHelp(self.root, key)


bst = RedBlackTree()

bst.insert(55)
bst.insert(40)
bst.insert(65)
bst.insert(60)
bst.insert(75)
bst.insert(57)

bst.delete(40)

print(bst.searchTree(60))



