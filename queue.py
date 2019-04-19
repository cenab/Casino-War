class Queue:
  def __init__(self):
    self.items = []
  def enqueue(self, item):
    self.items.insert(0,item)
  def isEmpty(self):
      return self.items == []
  def dequeue(self):
    return self.items.pop()
  def size(self):
    return len(self.items)
  def show(self):
    print (self.items)
  def __str__(self):
    return str(self.items)
