

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
        self.sum =0
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
    def Power(self,node):
        self.sum = 0
        self._Power(node)
        return self.sum
    def _Power(self,node,level=0):
        if node!= None:
            self._Power(node.left,level +1)
            self.sum += node.data
            self._Power(node.right,level+1)
inp = list(input("Enter Input : ").split("/"))
p = list(map(int,inp[0].split(" ")))
q = inp[1].split(",")
T = BST()
n = []

for i in range(len(q)):
    q[i] = list(map(int,q[i].split(" ")))
for i in p:
    n.append(Node(i))


for i in range(len(n)):
    if 2*i+1 < len(n):
        n[i].left = n[2*i+1]
    if 2*i+2 < len(n):
        n[i].right = n[2*i+2]

print(T.Power(n[0]))

for i in range(len(q)):
    if T.Power(n[q[i][0]]) > T.Power(n[q[i][1]]):
        print(str(q[i][0])+">"+str(q[i][1]))
    elif T.Power(n[q[i][0]]) < T.Power(n[q[i][1]]):
        print(str(q[i][0])+"<"+str(q[i][1]))
    else:
        print(str(q[i][0])+"="+str(q[i][1]))