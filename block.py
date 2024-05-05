import hashlib
import time


class Block:
    def __init__(self, index, previous_hash, autor, recebedor, message):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.autor = autor
        self.recebedor = recebedor
        self.message = message
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.timestamp) + str(self.previous_hash) + str(self.autor) + str(self.recebedor) + str(self.message)
        return hashlib.sha256(data.encode()).hexdigest()
