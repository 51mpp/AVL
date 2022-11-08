class root:

    def __init__(self, data): 

        self.data = data  

        self.left = None  

        self.right = None 

        self.level = None 



    def __str__(self):

        return str(self.data) 



class Tree:

    def __init__(self): 

        self.root = None

        self.num = 0



    def insert(self, val):  

        if self.root == None:

            self.root = root(val)

            self.num += 1

        else:

            h = height(self.root)

            max_root = pow(2,h+1)-1

            current = self.root

            if self.num+1 > max_root:

                while(current.left != None):

                    current = current.left

                current.left = root(val)

                self.num+=1

            elif self.num+1 == max_root:

                while(current.right != None):

                    current = current.right

                current.right = root(val)

                self.num+=1

            else:

                #print(max_root-((max_root-(pow(2,h)-1))/2))

                if self.num+1 <= max_root-((max_root-(pow(2,h)-1))/2):

                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)

                else:

                    insert_subtree(current.right,self.num - pow(2,h),val)

                self.num+=1

                    

def insert_subtree(r,num,val):

    if r != None:

        h = height(r)

        max_root = pow(2,h+1)-1

        current = r

        if num+1 > max_root:

            while(current.left != None):

                current = current.left

            current.left = root(val)

            return

        elif num+1 == max_root:

            while(current.right != None):

                current = current.right

            current.right = root(val)

            return

        if num+1 <= max_root-((max_root-(pow(2,h)-1))/2):

            insert_subtree(current.left,num - round(pow(2,h)/2),val)

        else:

            insert_subtree(current.right,num - pow(2,h),val)

    else:

        return



def height(root):

    if root == None:

        return -1

    else:

        left = height(root.left)

        right = height(root.right)

        if left>right:

            return left + 1

        else:

            return right + 1

                       

def printTree90(root, level = 0):

    if root != None:

        printTree90(root.right, level + 1)

        print('     ' * level, root)

        printTree90(root.left, level + 1)

def findMax(root):
    while root.right:
        root = root.right
    return root.data
def findMin(root):
    while root.left:
        root = root.left
    return root.data
def check_binary_search_tree_(root):
    #code here
    if (root == None):
        return True
 
    if root.left != None and findMax( root.left) >= root.data  :
        return False
 
    if root.right != None and findMin( root.right) <= root.data :
        return False
    if root.left != None and root.left.data>100:
        return False
    if root.right != None and root.right.data<0:
        return False
    if root.left != None and root.left.data<0:
        return False
    if root.right != None and root.right.data>100:
        return False
    if root != None and (root.data <0 or root.data>100):
        return False    
    if not check_binary_search_tree_(root.left) or not check_binary_search_tree_(root.right):
        return False
    return True

tree = Tree()

data = input("Enter Input : ").split()

for e in data:

    tree.insert(int(e))

printTree90(tree.root)

print(check_binary_search_tree_(tree.root))