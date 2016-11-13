class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self,newData):
        self.data =  newData
    
    def setNext(self,newNext):
        self.next = newNext
    
    def __str__(self):
        return str(self.data)


class UnorderedList:
    
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        flag = False
        while current != None and flag == False:
            if (current.getData() == item):
                flag = True
            else:
                current = current.getNext()
        return flag

    #Assuming that the element we are looking for is present in the list. 
    
    def remove(self,item):
        current = self.head
        previous = None
        flag = False
        while not flag:
            if (current.getData() == item):
                flag = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    
        


mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))
        
