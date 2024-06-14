
class Iterator:
    def __init__(self, data):
        pass

    def __next__(self):
        pass

    def hasNext(self):
        pass

class JSONIterator(Iterator):
    def __init__(self, json_data):
        self.stack = json_data[::-1]

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        nextNode = self.stack.pop()
        return nextNode
    

class IteratorCollection():
    def create_Iterator(self):
        return Iterator()

class JSONIteratorCollection(IteratorCollection):
    def create_Iterator(self, data):
        return JSONIterator(data)