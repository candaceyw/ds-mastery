# Stacks uses Arrays or Linked lists
# Queues uses Arrays or LInked lists
# Linked lists has more dynamic memory
# arrays are not a good choice for queues


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
            self.last = self.first
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def dequeue(self):
        temp = self.first.next
        dequeued_element = self.first
        if temp == None:
            self.first = None
            self.length -= 1
            return
        self.first.next = None
        self.first = temp
        self.length -= 1

    def print(self):
        temp = self.first
        while temp != None:
            print(temp.value, end='->')
            temp = temp.next
        print()
        print(self.length)


myq = Queue()
myq.enqueue('google')
myq.enqueue('microsoft')
myq.enqueue('facebook')
myq.enqueue('apple')
myq.print()
myq.dequeue()
myq.print()
x = myq.peek()
print(x)
