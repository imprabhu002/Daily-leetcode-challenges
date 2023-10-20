class NestedIterator:
    def __init__(self, nestedList):
        # Initialize the stack to hold iterators
        self.stack = [iter(nestedList)]
        # Initialize the current value to None
        self.current = None

    def next(self):
        # If there's a current value, return it and set current to None
        if self.current is not None:
            result = self.current
            self.current = None
            return result

        # Keep popping the stack until an integer is found
        while self.stack:
            try:
                # Try to get the next element from the current iterator
                element = next(self.stack[-1])
                # If it's an integer, return it
                if element.isInteger():
                    return element.getInteger()
                # If it's a list, push its iterator to the stack
                self.stack.append(iter(element.getList()))
            except StopIteration:
                # If the current iterator is exhausted, pop it from the stack
                self.stack.pop()
        return None

    def hasNext(self):
        # If there's a current value, return True
        if self.current is not None:
            return True

        # Keep popping the stack until an integer is found or the stack is empty
        while self.stack:
            try:
                element = next(self.stack[-1])
                if element.isInteger():
                    # If an integer is found, set current and return True
                    self.current = element.getInteger()
                    return True
                self.stack.append(iter(element.getList()))
            except StopIteration:
                self.stack.pop()
        return False
