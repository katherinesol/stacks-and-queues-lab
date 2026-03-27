import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # add item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # remove and return item from the front
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        # return front item without removing it
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        # return True if queue has no items
        return len(self.items) == 0

    def select_and_announce_winner(self):
        # randomly select a winner from the queue
        if self.is_empty():
            return None
        
        # pick a random winner from current items
        winner = random.choice(self.items)
        
        # dequeue everyone up to and including the winner
        while not self.is_empty():
            customer = self.dequeue()
            if customer == winner:
                break
        
        return winner