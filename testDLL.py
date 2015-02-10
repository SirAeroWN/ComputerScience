from DoublyLinkedListClass import *

def outputList(L):
    current = L.head
    while current != None:
        print(current.data, end = " ")
        current = current.next
    print ("\n")
    return

aDLL = DoublyLinkedList()

aDLL.addToRear("First")
aDLL.addToRear("Second")
outputList(aDLL)
aDLL.addToFront("Third")
outputList(aDLL)
aDLL.addToRear("Fourth")
aDLL.addToFront("Fifth")
outputList(aDLL)
aDLL.removeFromFront()
outputList(aDLL)
aDLL.removeFromRear()
outputList(aDLL)
