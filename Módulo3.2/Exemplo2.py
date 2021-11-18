class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.fila = []

    def put(self, elem):
        self.fila.append(elem)

    def get(self):
        if len(self.fila) == 0:
            raise QueueError
        elem = self.fila[0]
        del self.fila[0]
        return elem

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")