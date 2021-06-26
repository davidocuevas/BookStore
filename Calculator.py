import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator

class Calculator:
    def __init__(self) :
        self.expression = ""
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)

    def matched_expression(self, s : str) -> bool :
        stack = ArrayStack.ArrayStack()
        if len(s) == 0 or s[0] == ")":
            return False
        for item in s:
            if item == '(':
                stack.push(item)
            elif item == ')' and stack.size() > 0:
                stack.pop()
            elif item == ')' and stack.size() == 0:
                return False

        if stack.size() == 0:
            return True
        else:
            return False

    def set_expression(self, x: str):
        self.set_expression = x

###############################################################################################################
    def build_parse_tree(self, exp : str) -> str:
        # todo
        if not self.matched_expression(exp):
            return None
        t = BinaryTree.BinaryTree()
        t.r = t.Node('')
        u = t.r
        for token in exp:
            if token == '(':
                u = u.insert_left()
            elif token in '+-*/':
                u.x = token
                u = u.insert_right()
            elif token.isalpha():
                u.x = token
                u = u.parent
            elif token == ')':
                u = u.parent
        return t

#################################################################################################################
    def _evaluate(self, root):
        op = { '+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        # todo
        left = root.left
        right = root.right
        if left != None and right != None:
            opp = op[root.x]
            return opp(self._evaluate(left), self._evaluate(right))
        elif left == None and right == None:
            t = self.dict.find(root.x)
            if t != None:
                return t
            return root.x
        else:
            if left != None:
                return float(self._evaluate(left))
            else:
                return float(self._evaluate(right))

    def evaluate(self, exp):
        if self.dict.size() == 0:
            return 0
        parseTree = self.build_parse_tree(exp)
        return float(self._evaluate(parseTree.r))

    def swap(self, exp: str): #Implemented another method...
        a = ""
        for i in self.expression:
            if self.dict.find(i) is not None:
                i = self.dict.find(i)
                a += i
            else:
                a += i
        print(a)
        pass


