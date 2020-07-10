class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.stack = []
        self.stack2 = []

    def add(self, num: int):
        self.value = self.value + num
        self.stack.append((1, num))

    def subtract(self, num: int):
        self.value = self.value - num
        self.stack.append((-1, num))
    def undo(self):
        if len(self.stack) <= 0:
            return
        element = self.stack.pop()
        operation = element[0]
        num = element[1]
        self.stack2.append( element)

        if operation == 1:
            if self.value > 0:
                self.value = self.value - num



        if operation == -1:
            self.value = self.value + num

    def redo(self):
        if len(self.stack2) <= 0:
          return
       element = self.stack2.pop()
       operation = element[0]
       num = element[1]
       self.stack.append( element )

       if(operation == 1):
           self.value = self.value + num

       if(operation == -1):
           if self.value > 0:
               self.value = self.value - num    
    def bulk_undo(self, steps: int):
        passwhile steps > 0 and len(self.stack) > 0:
            self.undo()
            steps = steps - 1

    def bulk_redo(self, steps: int):
        while steps > 0 and len(self.stack2) > 0:
            self.redo()
            steps = steps - 1
