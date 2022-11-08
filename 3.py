

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.root = None
        self.order = -1
        self.fin = False
    def insert(self, data):
        self.root = BST._insert(self.root,data)
    def _insert(root, data):
        if root == None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._insert(root.left,data)
            else:
                root.right = BST._insert(root.right,data)
            x = root
            return root
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def preOrder(self,node):
        if node!= None:
            print(node.data,end="")
            self.preOrder(node.left)
            self.preOrder(node.right)
    def inOrder(self,node,level=0):
        if node!= None:
            if node.right !=None and node.left !=None: 
                print("(",end="")
            self.inOrder(node.left,level + 1)
            self.order +=1
            print(node.data,end=" ")
            self.inOrder(node.right, level + 1)
            if node.right !=None and node.left !=None: 
                print(")",end="")
    def Ranking(self,data):
        self.order = -1
        self.fin = False
        if isExit(self.root,data):
            self.order +=1
        self.insert(data)
        self._Rank(self.root,data)
        return self.order
    def _Rank(self,node,data,level=0):
        if node!= None:
            self._Rank(node.left,data,level +1)
            if self.fin == True:
                return
            self.order +=1
            #print(node.data,data,self.order)
            if node.data == data:
                self.fin = True
            self._Rank(node.right,data,level+1)

def isExit(root,data):
    if root == None:
        return False
    if root.data == data:
        return True
    if data < root.data:
        return isExit(root.left, data)
    else:
        return isExit(root.right, data)

inp = list(input("Enter Input : ").split("/"))
p = list(map(int,inp[0].split(" ")))
T = BST()
for i in p:
    T.insert(int(i))
#T.inOrder(T.root)
T.printTree(T.root)
print("--------------------------------------------------")
print("Rank of",inp[1],": ",end="")
print(T.Ranking(int(inp[1])))