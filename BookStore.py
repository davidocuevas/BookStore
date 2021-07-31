# Not all the imports are nessesary for this program to function, It depends on which data structure is being used.
import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree 
import BinaryHeap 
import AdjacencyList
import AdjacencyMatrix
import MaxQueue
import time
import algorithms



class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self) :
        self.bookCatalog = None
        self.shoppingCart = SLLQueue.SLLQueue()
        self.bookSortedCatalog = None
        #self.similarGraph = None
        self.sortedTitle = None
        self.indexKeys = None
        #self.indexSortedTitle = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        self.indexTitle = ChainedHashTable.ChainedHashTable()
        self.sortedTitle = ChainedHashTable.ChainedHashTable()
        self.bookSortedCatalog = ArrayList.ArrayList()
        self.indexKeys = ChainedHashTable.ChainedHashTable()
        #self.searchTree = BinarySearchTree.BinarySearchTree()
        #self.similarGraph = AdjacencyList.AdjacencyList(self.bookCatalog.size())
        with open(fileName, encoding='UTF8') as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            i = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                self.indexKeys.add(s.key, i)
                i+=1
        self.similarGraph = AdjacencyList.AdjacencyList(self.bookCatalog.size())
        with open(fileName, encoding="UTF8") as f:
            i = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                l = similar.split()
                for k in range(1,len(l)):
                    j = self.indexKeys.find(l[k])
                    if j is not None:
                        self.similarGraph.add_edge(i,j)
                i += 1
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")
    
    def setShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = SLLQueue.SLLQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")


    def removeFromCatalog(self, i : int) :
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix : str) :
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        index = -1
        if infix == None:
            raise IndexError("Error")
        else:
            for k in self.bookCatalog:
                index += 1
                if infix == "":
                    print (f"{k.title} is at index {index}")
                    if index >= 49:
                        break
                elif infix in k.title:
                    print(f"{k.title} is at index {index}")
            elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self) :
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getbestseller(self):
        bestsell = MaxQueue.MaxQueue()
        for x in self.shoppingCart:
            bestsell.add(x)
        print("Best seller is:",bestsell.max())

    def reverseShoppingCart(self):
        start_time = time.time()
        self.shoppingCart.reverse()
        elapsed_time = time.time() - start_time
        print(f"Reversed ShoppingCart in {elapsed_time} seconds")

    def findFromIndexTitle(self, t: str):
        start_time = time.time()
        userbook = self.indexTitle.find(t)
        if userbook != None:
            self.shoppingCart.add(userbook)
            print(f"Found {userbook}")
        else:
            print(f"Sorry, {t} was not found. ")
        elapsed_time = time.time() - start_time
        print (f"Loading {self.indexTitle.size()} books in {elapsed_time} seconds")

    def searchByPrefix (self, t : str):
        start_time = time.time()
        book = self.searchTree.find(t)
        if t == "":
            print ("Sorry no book was found :(")
        elif book != None:
            self.shoppingCart.add(book)
            print(f"Found {book}")
        else:
            print(f"Sorry {book} was not found :(")
        elapsed_time = time.time() - start_time
        print(f" Loading books by Sorted Title in {elapsed_time} seconds")


    def BestSellingBook(self, infix: str):
        index = 0
        best = BinaryHeap.BinaryHeap()
        counter = 0
        for i in self.bookCatalog:
            index += 1
            if infix == "":
                print("No books found")
                if index >= 1:
                    break

            if infix in i.title:
                x = i.rank * -1
                best.add(Book.Book(i.key,i.title,i.group,x,i.similar))

        for j in range(len(best)):
            r = best.remove()
            print(str(r.rank * -1), ": ",r.title)
            counter += 1
            if counter == 10:
                break

    def SortableBooks(self, prefix, choice: int):
        start_time = time.time()
        if prefix == "":
            print("No Book Was Entered")
            return
        mergeArray = []
        quickArray = []
        index = -1
        for i in self.bookCatalog:
            index += 1
            if prefix in i.title:
                a = index, i.title
                if choice == 0:
                    mergeArray.append(a)
                if choice == 1:
                    quickArray.append(a)
        if choice == 0:
            print("Merge Sorted", algorithms.merge_sort(mergeArray))
        elif choice == 1:
            print("Quick Sorted", algorithms.quick_sort(quickArray))
        elapsed_time = time.time() - start_time
        print(f" Sorting books completed in {elapsed_time} seconds")

    def binarySearchTitle(self, prefix: str):
        titleCatalog = ArrayList.ArrayList()
        for i in range(self.SortableBooks.size()):
            titleCatalog.append(self.SortableBooks.get(i).title)
        algorithms.merge_sort(titleCatalog)
        index = algorithms.binary_search(titleCatalog, prefix)
        while index is not None:
            algorithms.binary_search(titleCatalog, prefix)
            if index is not None:
                print(titleCatalog.get(index))
                titleCatalog.remove(index)
