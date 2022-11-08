



class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None
    def closest(self,data):
        return BinarySearchTree._closest(self.root,data)   
    def _closest(root,data,diff=None,min=None):
        print(min)
        print(diff)
        print(root.data)
        
        if root == None:
            return min
        else:
            if min==None or abs(root.data - data) < diff:
                diff = abs(root.data - data)
                min = root.data 
            if data < root.data:
                print("left")
                return BinarySearchTree._closest(root.left,data,diff,min)
            else:
                print("right")
                return  BinarySearchTree._closest(root.right,data,diff,min)
            
            

    def insert(self, data):
        self.root = BinarySearchTree._insert(self.root,data)
    def _insert(root, data):
        if root == None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BinarySearchTree._insert(root.left,data)
            else:
                root.right = BinarySearchTree._insert(root.right,data)
            return root
    def findsuccessor(self, root):
        minimum = root.data
        while root.left != None:
            minimum = root.left.data
            root = root.left
        return minimum
    def Delete(self, root, data):
        if isExit(root,data) == False:
            print("Error! Not Found DATA")
        self.root = self.delete(root, data)
    def delete(self, root, data):
        if root == None:
            return root
        if data == root.data:
            
            if root.left == None:
                root = root.right
            elif root.right == None:
                root = root.left
            else:
                root.data = self.findsuccessor(root.right)
                root.right = self.delete(root.right, root.data)
        elif data < root.data:
            root.left = self.delete(root.left, data)
        else:
            root.right = self.delete(root.right, data)
        return root
def isExit(root,data):
    if root == None:
        return False
    if root.data == data:
        return True
    if data < root.data:
        return isExit(root.left, data)
    else:
        return isExit(root.right, data)
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
def close(root,data,diff=None,min=None):
        
        if root == None:
            return min
        else:
            if min==None or abs(root.data - data) < diff:
                diff = abs(root.data - data)
                min = root.data 
            if data < root.data:
                #print("left")
                return close(root.left,data,diff,min)
            else:
                #print("right")
                return  close(root.right,data,diff,min)

T = BinarySearchTree()

inp = list(input("Enter Input : ").split("/"))
p = list(map(int,inp[0].split(" ")))


for i in p:
    T.insert(int(i))
    printTree90(T.root)
    print("--------------------------------------------------")

print("Closest value of "+inp[1]+" : "+str(close(T.root,int(inp[1]))))