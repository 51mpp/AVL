
class Node:
    def __init__(self,data,freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
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
def nodeSort(olist:list):
    nlsit = []
    min = olist[0]
    while len(olist) != 0:
        for  i in olist:
            if i.data< min.data:
                min = i 
        nlsit.append(min)
        print(len(olist))
        olist.remove(min)
        print(len(olist))
    return nlsit
def sortses(olist:list):
    for i in range(len(olist)):
        for j in range(len(olist)-1):
            if olist[j].freq>olist[j+1].freq:
                olist[j+1],olist[j] = olist[j],olist[j+1]
            if olist[j].freq==olist[j+1].freq :
                if olist[j+1].data =='*' :
                    olist[j+1],olist[j] = olist[j],olist[j+1]
                else:
                    if olist[j].data>olist[j+1].data and olist[j] != '*':
                        olist[j+1],olist[j] = olist[j],olist[j+1]
    return olist
def second(el):
    return el[1]
def printCode(node, code):
    s = ''
    if node:
        s = printCode(node.right, code + '1')
        if node.data != '*':
            s += "'" + str(node.data) + "': '" + code + "'"
        a = printCode(node.left, code + '0')
        if a != '':
            s += ', ' + a
    return s
def Encode(node, data, code): 
    if node ==None:
        return None
    if data == node.data:
        return code
    if node:
        s = Encode(node.right, data, code + '1')
        if s != None:
            return s
        s = Encode(node.left, data, code + '0')
        return s
T = BST() 
inp = input("Enter Input : ")
chr = []
cnt = []
num = []
for i in inp:
    if i not in chr:
        chr.append(i)

for i in chr:
    cnt.append([i,0])

for i in inp:
    for j in range(len(chr)):
        if i == cnt[j][0]:
            cnt[j][1]+=1

            
for i in range(len(cnt)):
        for j in range(len(cnt)-1):
            if cnt[j][1]>cnt[j+1][1]:
                cnt[j+1],cnt[j] = cnt[j],cnt[j+1]
            elif cnt[j][1]==cnt[j+1][1] :
                if cnt[j][0]>cnt[j+1][0]:
                    cnt[j+1],cnt[j] = cnt[j],cnt[j+1]   
            
for i in range(len(cnt)):
        num.append(Node(cnt[i][0],int(cnt[i][1])))
num.reverse()
temp = []
temp.append(num.pop())
print(temp)

while len(temp) !=1 or len(num) !=0:
    for i in temp:
        print(i.data)
    print("***********")
    if len(temp)>1:
        if num==[] or (num[-1].freq>=temp[0].freq +temp[1].freq):
            a = temp.pop(0)
            b = temp.pop(0)
            c = a.freq+b.freq
            c = Node('*',c)
            c.left = a
            c.right = b
            temp.append(c)
        else:
            temp.append(num.pop())
    else:
        temp.append(num.pop())

print('{' + f'{printCode(temp[0], "")}' + '}')
T.printTree(temp[0])
print('Encoded! : ', end = '')
for i in inp:
    print(Encode(temp[0], i, ''), end = '')

