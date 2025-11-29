from circularqueue import CircularQueue

class Tnode:
    def __init__(self, data, Llink = None , Rlink = None):
        self.data = data
        self.Llink = Llink
        self.Rlink = Rlink
        
def preorder(n):
    if n is not None:
        print(n.data, end = ' ')
        preorder(n.Llink)
        preorder(n.Rlink)
            
def inorder(n):
    if n is not None:
        inorder(n.Llink)
        print(n.data, end = '')
        inorder(n.Rlink)
        
def postorder(n):
    if n is not None:
        postorder(n.Llink)
        postorder(n.Rlink)
        print(n.data, end = ' ')
        
def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end = ' ')
            queue.enqueue(n.Llink)
            queue.enqueue(n.Rlink)
            
def count_leaf(n):
    if n is None:
        return 0
    elif n.Llink is None and n.Rlink is None:
        return 1
    else:
        return 1 + count_node(n.Llink) + count_node(n.Rlink)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.Llink) + count_node(n.Rlink)            

def calc_height(n):
    if n is None:
        return 0
    hleft = calc_height(n.Llink)
    hright = calc_height(n.Rlink)
    if (hleft > hright):
        return hleft + 1
    else:
        return hright + 1
     
    '''   
d = Tnode('D', None, None)
e = Tnode('E', None, None)
b = Tnode('B', d, e)
f = Tnode('F', None, None)
c = Tnode('C', None, None)
root = Tnode('A', b, c)

print('\n   In-order : ', end = '')
inorder(root)
print('\n  Pre-order : ', end = '')
preorder(root)
print('\n Post-order : ', end = '')
postorder(root)
print('\nLevel-order : ', end = '')
levelorder(root)
print()

print('노드의 개수 = %d개' %count_node(root))
print('단말 개수 = %d개' %count_leaf(root))
print("트리의 높이 = %d개" %calc_height(root))'''