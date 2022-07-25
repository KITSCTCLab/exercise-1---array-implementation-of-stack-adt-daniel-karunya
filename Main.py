import os


class Stack:
    """
    Description : The slass stack is used to implement stack adt using list functions.

    Attributes :-
    self.items : list of items in stack
    items.size: max size of stack

    """

    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        """
        Description : Checks if stack is empty
        Arguments : self
        Returns :true or false based on the result

        """
        if len(self.items) == 0:
            return True
        else:
            return False

    def is_full(self):
        """
        Description : Checks if stack is full
        Arguments : self
        Returns : True or false based on the results

        """
        if len(self.items) == self.size:
            return True
        else:

            return False

    def push(self, data):
        """
        Description : Adds data to top of stack based on the redult of the  isfull() function to check if stack is full
        Arguments : self,data
        Returns :data if push success

        """
        if not self.is_full():
            self.items.append(data)

    def pop(self):
        """
        Description : Removes data to top of stack based on the redult of the  isempty() function to check if stack is empty
        Arguments : self
        Returns :popped element

        """
        popped = 0
        if not self.is_empty():
            popped = self.items.pop(len(self.items) - 1)
        return popped

    def status(self):

        """
        Description : prints stack in order
        Arguments : self
        Returns :nil

        """
        for i in range(0, (len(self.items))):
            print(self.items[(i)])


# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
