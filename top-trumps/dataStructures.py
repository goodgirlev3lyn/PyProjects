# To use: create a folder, put your main.py inside that folder and put this module inside there too
# In main.py:
# from dataStructures import Stack, Queue <- Optional, don't use * unless needed
#
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡖⠀⡔⠀⠀⠀⠀⠀⠰⡰⡀⠀⠀⢳⣄⠀⠀⠐⠆⠀⠀⠀⠀⠀⠐⢆⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⢀⡔⠛⠛⢯⡉⠑⠒⡤⠊⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⣀⣀⡀⠤⠤⠤⠤⠤⠼⠤⢴⣃⡀⠀⠀⠀⠀⠀⢳⢱⡀⠀⠀⢳⡱⣄⠀⠀⠐⢄⠀⠀⠀⠀⠈⢣⠀⠀⠀⠀
#⠀⠀⠀⠀⢠⠋⠀⠀⣀⣀⢳⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠦⣄⠀⠈⡇⢣⠀⠀⠀⢣⠈⢦⠀⠀⠀⠑⢄⠀⠀⠀⠀⢣⡀⠀⠀
#⠀⠀⠀⢠⣃⠴⠊⠉⢀⡴⡻⢹⠘⠢⢄⣀⣀⠴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⣱⠈⡇⠀⠀⠈⣇⠀⢷⡀⠀⠀⠈⠳⡀⠀⠀⠀⢳⡀⠀
#⠀⠀⢀⠏⠁⠀⠀⢠⠎⡰⠁⠘⡄⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣽⠀⠀⠀⢸⠀⢸⡵⡀⠀⠀⠀⠘⢆⠀⠀⠀⢣⠀
#⠀⠀⡜⠀⠀⠀⢠⠏⢰⡇⠀⠀⢑⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠄⠒⠒⠒⠒⠂⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠈⡆⢸⢇⢱⡀⠀⠀⠀⠈⢦⠀⠀⠈⠀
#⠀⢠⠃⠀⠀⠀⡞⠀⣿⠁⠀⢠⠎⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠄⠀⠀⠤⠤⣀⡈⠑⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢄⠀⡇⢸⢸⠀⢧⠀⠀⠀⠀⠈⢧⣀⠴⠊
#⠀⠈⠀⠀⠀⢸⠁⢸⢸⠀⣰⠃⠀⠀⠀⠀⠀⠀⡴⠋⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⢄⠑⢄⠀⠀⠀⢦⠀⠀⠀⠀⠀⠀⠈⢦⡇⢸⠘⡄⠘⡆⠀⠀⣀⠴⠊⠁⢀⡰
#⠀⠀⠀⠀⠀⡇⠀⡎⢸⢠⠃⠀⠀⠀⠀⠀⢀⡞⠀⢠⠖⠁⠀⢤⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⣵⣄⠀⠀⠳⡀⠀⠀⠀⠀⠀⠀⢳⡌⠀⡇⠀⢷⡠⠊⠁⠀⣠⡔⡏⡜
#⠀⠀⠀⠀⢸⠀⠀⡇⢸⡎⠀⠀⠀⠀⠀⢀⡎⠀⡴⠁⠀⠀⠀⠀⢹⢦⡈⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⣄⠀⠹⡄⠀⠀⠀⠀⠀⠀⢻⣠⣃⡴⠋⠀⣠⠔⠊⠀⡇⢩⠞
#⠀⠀⠀⠀⡏⠀⠀⡇⡸⠀⠀⠀⠀⠀⠀⡞⠀⡜⠁⠀⠀⠀⠀⠀⢸⡆⠛⠦⡈⠢⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢆⠀⠘⡄⠀⠀⠀⠀⠀⠀⢻⡊⠀⣠⠊⠁⠀⠀⡜⢰⡇⠀
#⠀⠀⠀⢠⠃⠀⠀⣇⠇⠀⠀⠀⠀⠀⢰⠁⡸⠁⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠈⠓⠬⡑⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀⠹⡀⠀⠀⠀⠀⢠⡀⢣⡜⠁⠀⠀⠀⢰⢱⠃⢸⠀
#⠀⠀⠀⢸⠀⠀⠀⢹⢠⠀⠀⠀⠀⠀⢸⢠⠃⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠈⠑⠲⠭⣲⡴⢖⣒⡆⠀⠀⠀⠀⠀⢧⠀⢳⠀⠀⠀⠀⠀⢧⠈⡆⠀⠀⠀⢠⢇⠇⠀⠸⠀
#⠀⠀⠀⡎⠀⠀⠀⡎⢸⠀⠀⠀⠀⠀⢿⡜⠀⠀⠀⠀⠀⠀⡀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⢉⡡⠞⠛⢭⣭⣥⠤⠤⠚⡆⠈⣦⠆⠀⠀⠀⠸⠀⢳⠀⠀⠀⡞⡞⠀⠀⠀⠀
#⠀⠀⠀⡇⠀⠀⢰⡇⢸⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⢠⡏⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠉⠉⣠⠖⠋⠁⢀⣤⣤⣦⣔⣳⡾⢳⠀⠀⠀⠀⠀⡇⢸⣀⡠⠊⣼⢸⠀⠀⠀⠀
#⠀⠀⠀⡇⠀⠀⢸⡇⢸⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⢀⡮⣵⠓⢠⡤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡝⢀⣴⣯⣿⡿⣛⣿⣿⣻⡄⢸⠀⠀⠀⠀⢀⡇⠸⠣⣄⡜⠁⢸⠀⠀⠀⠀
#⠀⠀⠀⡇⠀⠀⡇⠇⢸⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⢴⣱⣷⣁⢤⣊⣀⡀⠙⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⡿⠁⢿⣄⡿⠟⣸⡛⡇⡎⠀⠀⠀⠀⢸⣵⢐⣴⠋⠀⠀⠈⠀⠀⠀⠀
#⠯⣉⠀⠓⠒⠒⠃⢼⠸⡄⠀⠀⠀⠀⠀⠸⡀⠀⢀⣼⠏⡠⠞⠁⠀⠈⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠐⣲⡾⠏⠀⣧⢣⠀⠀⠀⠀⡎⣿⣼⢸⡆⠀⠀⠀⠀⠀⠀⠀
#⠣⢌⡻⣍⣱⠒⡠⢼⠀⡇⠀⠀⠀⠀⠀⠀⢧⡠⠚⠁⠘⢁⣤⣶⣶⣶⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⢸⠀⠀⠀⢰⢹⡜⣿⣿⢣⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠉⢲⣄⡀⢣⡈⡇⢹⠀⠀⠀⠀⠀⢢⠘⡄⢄⣀⣠⣾⠟⢹⣏⡈⣿⡿⣿⠲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⢸⠀⠀⢠⢃⡏⡇⡿⣹⢸⡀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⢸⣡⠉⡶⣍⢳⠀⣇⠀⠀⠀⠀⠈⣆⠻⣄⠀⠉⠙⢦⣀⠉⠹⠧⣤⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⢸⠀⣠⠃⡞⡇⡇⠀⡟⡞⠁⠀⠀⠀⠀⢀⠀
#⠀⠀⠀⠀⡿⠀⡇⠀⠹⡄⢸⡄⠀⠀⠀⠀⠘⡄⢣⠳⣄⠀⠀⠀⠋⠚⠙⠉⠁⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⢸⡰⠁⡜⠁⡗⢸⠀⢹⠃⠀⠃⠀⠀⠀⠸⠀
#⠀⠀⠀⠀⢧⡇⠃⠀⠀⢳⠈⡿⡀⠀⠀⠀⠀⠘⣆⢳⡌⣢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢯⣼⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⢁⡞⠀⢰⠃⣼⠀⢸⠀⠀⠀⠀⠀⠀⡇⠀
#⠀⠀⠀⠀⢸⢡⠀⠀⠀⠈⢧⢱⢱⡀⠀⠀⠀⠀⢹⢫⣫⡁⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⢀⡾⠁⠀⡜⢠⢻⠀⢸⠀⠠⠀⠀⠀⢠⠃⠀
#⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠈⣎⢿⠙⣄⠀⠀⠀⠈⣿⢯⠳⣄⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠐⠊⠁⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⣼⢥⠏⡸⠀⡎⡄⠀⠀⠀⠀⡸⠀⠀
#⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⢸⢞⣞⡞⢳⡀⠸⡄⠛⡌⣦⠏⠷⠄⠀⠑⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⣠⡾⡿⠋⢀⡇⢀⢧⠃⠀⠀⠀⠀⡇⠀⠀
#⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⢸⢸⣿⣦⣞⠏⠢⣱⢀⢧⢹⠀⠀⠀⠀⠀⠀⠈⠉⠒⠒⠠⠤⠤⢀⣀⣀⣀⠀⠀⠀⢀⡠⠞⠁⢀⣠⣾⣿⢾⡀⠀⠘⠀⢸⡜⠀⠀⠀⠀⠘⠀⡸⠀
#⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⢸⢸⠿⡫⠋⠀⠀⠈⡟⠈⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⢿⣿⠯⠥⠤⠒⣎⡿⢿⡿⠳⡀⠑⣄⠀⠀⣏⠃⠀⠀⠀⠀⠀⢠⠃⠀
#⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⢸⡈⠉⠀⠀⠀⠀⠀⠇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢹⠍⢹⠉⢹⠀⠀⢀⣳⡄⠙⢄⠈⢢⣰⡻⠀⠀⠀⠀⠀⠀⡞⠀⠀
#⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⠀⣸⠎⠉⠓⠢⢜⣆⠈⢣⡀⢹⠇⠀⠀⠀⠀⠀⢠⠃⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⡿⡄⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡃⢸⡴⢻⠀⣀⣠⣤⣶⣾⣧⡀⠑⡼⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀
#⠀⠀⡆⠀⠀⠀⠀⢸⢣⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠟⡇⢸⣟⢿⡿⠿⠿⠿⠛⣷⣄⡇⠀⠀⠀⠀⠀⠀⡇⠀⡴⠀
#⠀⠀⢱⠀⠀⠀⠀⠈⡎⡆⠀⠀⡷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⡇⢸⡇⠀⠀⣀⡠⠤⠖⠛⠚⡇⠀⢠⠀⠀⠀⢠⠃⢰⠃⠀

"""
Docstrings needed on the methods, and change private attributes to _attr, aside from that these data structures are perfect
"""


# <----START OF STACK----> #
from typing import Any

class Stack:
    def __init__(self, maxSize: int) -> None:
        self.MaxSize: int = maxSize
        self.stack: list = [] # Implementing as a list
        for i in range(maxSize):
            # Initialize stack so no OutOfRange Exceptions
            self.stack.append(None)
        self.topPtr: int = 0

    def isFull(self) -> bool:
        return self.topPtr == self.MaxSize

    def isEmpty(self) -> bool:
        return self.topPtr == 0

    # Return True if successful, False if not
    def push(self, item: Any) -> bool:
        if self.isFull():
            print("Error - Stack is Full")
            return False
        else:
            self.stack[self.topPtr] = item
            self.topPtr += 1
            return True

    def pop(self) -> Any:
        if self.isEmpty():
            print("Error - Stack is Empty")
            return
        else:
            self.topPtr -= 1
            data = self.stack[self.topPtr]
            self.stack[self.topPtr] = None
            return data

    def peek(self) -> Any:
        if self.isEmpty():
            print("Error - Stack is Empty")
            return
        else:
            return self.stack[self.topPtr-1]

    def help(self):
        print("s = Stack(size)\ns.push(data)\ns.pop() <- returns bool if successful\ns.isEmpty()\ns.isFull()\ns.peek()\nprint(s)\ns.size()\ns.clear()")

    def __str__(self) -> str:
        return str(self.stack[:self.topPtr])

    def size(self) -> int:
        return self.topPtr

    def clear(self) -> None:
        self.stack = [None] * self.MaxSize
        self.topPtr = 0

# <----END OF STACK----> #


# <-----START OF QUEUE----> #

class Queue:
    def __init__(self, maxSize: int) -> None:
        self.Queue: list = [] # Implement as a list
        self.MaxSize: int = maxSize
        for i in range(self.MaxSize):
            # Initialize queue so no OutOfRange errors
            self.Queue.append(None)
        self.bottomPtr: int = 0 # <- bottom pointer ->
        self.topPtr: int = 0    # <- top    pointer ->
        self.itemAmount: int = 0 # Amount of items in queue

    def getSize(self) -> int:
        return self.itemAmount

    def isFull(self) -> bool:
        return self.itemAmount == self.MaxSize

    def isEmpty(self) -> bool:
        return self.itemAmount == 0

    def enQueue(self, data: Any) -> bool:
        """
        Returns true on success, else returns false if queue is full
        """
        if self.isFull() == True:
            print("Error - queue is Full")
            return False
        else:
            self.Queue[self.topPtr] = data
            self.topPtr += 1
            if self.topPtr == self.MaxSize:
                self.topPtr = 0
            self.itemAmount += 1
            return True

    def deQueue(self) -> Any:
        if self.isEmpty():
            print("Error - Queue is Empty")
            return
        else:
            data = self.Queue[self.bottomPtr]
            self.Queue[self.bottomPtr] = None
            self.bottomPtr += 1
            if self.bottomPtr == self.MaxSize:
                self.bottomPtr = 0
            self.itemAmount -= 1
            return data

    def peek(self) -> Any:
        if self.isEmpty():
            print("Error - Queue is Empty")
            return None
        return self.Queue[self.bottomPtr]

    def help(self):
        print("q = Queue(size)\nq.enQueue(data)\nq.deQueue() <- returns bool\nq.isEmpty()\nq.isFull()\nq.peek()\nprint(q)\nq.size()\nq.empty()")

    def __str__(self) -> str:
        items = []
        i = self.bottomPtr
        count = 0
        while count < self.itemAmount:
            items.append(str(self.Queue[i]))
            i = (i + 1) % self.MaxSize
            count += 1
        return "Queue: " + " <- ".join(items)   
    
    def size(self) -> int:
        return self.itemAmount

    def empty(self) -> None:
        self.itemAmount = 0
        self.topPtr = 0
        self.bottomPtr = 0
        self.Queue = [None] * self.MaxSize
    # declaration:
    # q = Queue(5 <- size)
    # q.isFull(), q.isEmpty(), q.enQueue(data), q.deQueue(), q.peek(), q.print()

# <-----END OF QUEUE----> #
