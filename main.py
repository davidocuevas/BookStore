import Calculator
import BookStore
import DLList
import SLLStack
import ChainedHashTable
import BinarySearchTree
import BinaryTree
import AdjacencyList
import AdjacencyMatrix

def menu_calculator() :
    calculator =  Calculator.Calculator()
    from ChainedHashTable import ChainedHashTable
    hash = ChainedHashTable()
    option=""
    while option != '0':
        print ("""
        1 Assign Values to Variables 
        2 Introduce expression (Check if expression is valid)
        3 Print expression
        4 Check matched expression 
        5 Print evaluated expression
        0 Return to main menu
        """)
        option=input()
        if option=="1":
            userin1= input("Please enter the variable: ")
            userin2= input("Please enter the number that will substitute the given variable: ")
            calculator.set_variable(userin1,float(userin2))

        if option=="2":
            expression = input("Introduce a mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"The written expression {expression} is valid!")
            else:
                print(f"{expression} is an invalid expression, try again.")

        elif option=="3":
            for i in expression:
                if calculator.dict.find(i) == None:
                    print(i,end='')
                else:
                    print(calculator.dict.find(i),end='')

        elif option =="4":
            expression = input("Introduce a mathematical expression: ")
            if expression == '':
                print("The expression is empty")
            elif calculator.matched_expression(expression):
                print (f"{expression} is a valid expression")
            else:
                print(f"{expression} is not a valid expression")

        elif option == "5":
            answer = float(calculator.evaluate(expression))
            print("%.2f" % answer)

        elif option=="0":
            main()

def menu_bookstore_system() :
    bookStore = BookStore.BookStore()
    option=""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Reverse shopping cart
        7 Get best seller 
        8 Find Book Through Index Title
        9 Search Tree
        10 Pre Order 
        11 In Order
        12 Post Order
        13 BF Traversal
        14 Tree Height
        15 Find the Catalog's best seller
        16 Sortable Books
        17 BFS2
        18 DFS2
        0 Return to main menu
        """)
        option=input() 
        if option=="r":
            bookStore.setRandomShoppingCart()
        elif option=="s":
            bookStore.setShoppingCart()
        elif option=="1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name) 
            #bookStore.pathLength(0, 159811)
        elif option=="2":
            i = int(("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option=="3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option=="4":
            bookStore.removeFromShoppingCart()
        elif option=="5":
            infix = input("Introduce the query to search: ")
            bookStore.searchBookByInfix(infix)
        elif option=="6":
            bookStore.reverseShoppingCart()
        elif option=="7":
            bookStore.getbestseller()
        elif option=="8":
            index_title = input("Enter the Index of the book you would like to find: ")
            bookStore.findFromIndexTitle(index_title)
        elif option=="9":
            find = input("Enter the prefix of the book you would like to find: ")
            bookStore.searchByPrefix(find)
        elif option == "10":
            l = []
            print(bookStore.searchTree.pre_order(bookStore.searchTree.r, l))
        elif option == "11":
            l = []
            print(bookStore.searchTree.in_order(bookStore.searchTree.r, l))
        elif option == "12":
            l = []
            print(bookStore.searchTree.post_order(bookStore.searchTree.r, l))
        elif option == "13":
            l = []
            print(bookStore.searchTree.bf_traverse())
        elif option == "14":
            l = []
            print(bookStore.searchTree.height())
        elif option == "15":
            swag = input("Introduce the query to search: ")
            bookStore.BestSellingBook(swag)
        elif option == "16":
            pfix = input("Enter a book index title: ")
            if pfix == "":
                print("No book was entered!")
                return menu_bookstore_system()
            print("""Sort Books Via.
            0 Merge Sort
            1 Quick Sort    
            """)
            choice = int(input())
            if choice == 0 or choice == 1:
                bookStore.SortableBooks(pfix, choice)
            else:
                print("Invalid")
                return menu_bookstore_system()
        elif option == "17":
            r = int(input("Enter the starting index: "))
            s = int(input("Enter the distance from the index: "))
            answer = bookStore.similarGraph.bfs2(r,s)
            for i in range(1, len(answer)):
                print(bookStore.bookCatalog.get(answer[i]))
        elif option == "18":
            r = int(input("Enter the starting index: "))
            s = int(input("Enter the destination: "))
            result = bookStore.similarGraph.dfs2(r,s)
            print("The degree of seperation is: ", result)
        ''' 
        Add the menu options when needed
        '''

def sllStackMenu():
    stack = SLLStack.SLLStack()
    option = ""
    while option != "0":
        print('''
                1 Add to SLLStack
                2 Remove from SLLStack
                3 Print SLLStack
                4 Reverse SLLStack
                0 Return to main menu
                ''')
        option = input()
        if option == "1":
            m = int(input("Enter an element to the SLLStack: "))
            stack.push(m)
        if option == "2":
            print(f"{stack.pop()} was removed from SLLstack: ")
        if option == "3":
            print("SSLStack: ", stack)
        if option == "4":
            stack.reverse()
            print(stack)

def menu_BinaryTree():
    bst = BinarySearchTree.BinarySearchTree()
    option = ""
    while option != "0":
        print('''
                    1 Add nodes and values for traversal
                    2 Values of Nodes pre order
                    3 Values of Nodes in order
                    4 Values of Nodes post order
                    5 Display values of bf_traversal
                    6 Print height of the tree
                    0 Return to main menu
                    ''')
        option = input()
        l = list()
        if option == "1":
            n = input("Enter the node you would like to add ")
            v = input("Enter the value you would like to add ")
            bst.add(n, v)
        if option == "2":
            print(bst.pre_order(bst.r, l))
        if option == "3":
            print(bst.in_order(bst.r, l))
        if option == "4":
            print(bst.post_order(bst.r, l))
        if option == "5":
            print(bst.bf_traverse())
        if option == "6":
            print(bst.height())

##################################################################_Used_This_For_testing
def chainedHashTable():
    table = ChainedHashTable.ChainedHashTable()
    option = ""
    while option != "0":
        print('''
                1 Add to Hash Table
                2 Remove from Hash Table
                3 Print Hash Table
                0 Return to main menu
                ''')
        option = input()
        if option == "1":
            n = int(input("Enter a key for the Hash Table: "))
            m = int(input("Enter an element to the Hash Table: "))
            table.add(n, m)
        if option == "2":
            k = int(input("Enter a key of an item you would like to remove for the Hash Table: "))
            print(f"{table.remove(k)} was removed from Hash Table: ")
        if option == "3":
            print("Hash Table: ", table)

def menu_dllist():
    dllist = DLList.DLList()
    option = ""
    while option != '0':
        print('''
            1 Add to DLList
            2 Remove from DLList
            3 Print DLList
            4 Check if Palindrome
            0 Return to main menu
            ''')
        option = input()
        if option=="1":
            i = int(input("Enter an element to the DLList: "))
            dllist.append(i)
        if option=="2":
            i = int(input("Enter the index of an element to remove from DLList: "))
            print(f"{dllist.remove(i)} at index {i} removed from DLList")
        if option=="3":
            print("DLList: ", dllist)
        if option=="4":
            testPalindrome()

def testPalindrome():
    testforPalindrome = DLList.DLList()
    test = input("Enter the word you would like to test if palindrome: ")
    for item in test:
        testforPalindrome.add(0, item)
    if testforPalindrome.isPalindrome():
        print(f"The word {test} is a palindrome!")
    else:
        print(f"The word {test} is not a palindrome!")

#main: Create the main menu
def main() :
    option=""
    while option != '0':
        print ("""
        1 Calculator
        2 Bookstore System
        3 DLList Menu
        4 SSLStack Menu
        5 Hash Menu 
        6 Binary Tree Menu
        0 Exit/Quit
        """)
        option=input() 
        
        if option=="1":
            menu_calculator()
        elif option=="2":
            menu_bookstore_system()
        elif option =="3":
            menu_dllist()
        elif option=="4":
            sllStackMenu()
        elif option=="5": #Not Needed
            chainedHashTable()
        elif option=="6":
            menu_BinaryTree()

if __name__ == "__main__":
  main()
