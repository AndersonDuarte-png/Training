class No:
    def __init__(self,item):
        self.item = item
        self.esquerda = None
        self.direita = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = No(data)
        if self.root is None:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if data < current_node.item:
                if current_node.esquerda is None:
                    current_node.esquerda = new_node
                    break
                current_node = current_node.esquerda
            else:
                if current_node.direita is None:
                    current_node.direita = new_node
                    break
                current_node = current_node.direita
    
    def pre_order_traversal(self):
        def traverse(node):
            if node is None:
                return
            
            traverse(node.esquerda)
            traverse(node.direita)
            print(node.item, end="")

        traverse(self.root)
        print()

entrada = input()
prefixo = []
infixo = []
pre = 1
for i in entrada:
    
    if pre == 2:
        infixo.append(i)
    
    if pre == 1:
        if i !=" ":
            prefixo.append(i)
        else:
            pre = 2

root = Tree()
for i in prefixo:
    root.insert(i)
root.pre_order_traversal()