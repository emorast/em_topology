
class Node:


    def __init__(self, toadd, next = None, prev = None):

        self.content = toadd
        self.next = None
        self.prev = None

        return

class Queue:

    def __init__(self):

        self.__head = None
        self.__tail = None
        self.length = 0

        return

    # Add to the end of queue
    def enqueue(self, toadd):

        tobeadded = Node(toadd)

        if self.__head == None:

            self.__head = tobeadded
            self.__tail = tobeadded

        else:

            self.__tail.next = tobeadded
            tobeadded.prev = self.__tail
            self.__tail = tobeadded

        return

    # Remove and return first node in queue
    def dequeue(self):

        toremove = self.__tail
        self.__tail = self.__tail.prev
        self.__tail.next = None

        return toremove

    # Print the queue in order
    def print(self):

        current_node = self.__head

        while current_node != None:

            print(current_node.content)

            current_node = current_node.next

        return


    def isEmpty(self):

        if self.length == 0:

            return True

        else:

            return False
