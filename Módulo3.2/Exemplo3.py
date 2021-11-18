class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.fila = []
    def put(self, elem):
        self.fila.append(elem)
    def get(self):
        elem = self.fila[0]
        del self.fila[0]
        return elem
    
class SuperQueue(Queue):
    def isempty(self):
        if len(self.fila) == 0:
            return True
        return False


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")