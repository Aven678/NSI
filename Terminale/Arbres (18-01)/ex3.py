class Arbre:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, leftTree):
        self.left = leftTree

    def set_right(self, rightTree):
        self.right = rightTree

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_data(self):
        return self.data