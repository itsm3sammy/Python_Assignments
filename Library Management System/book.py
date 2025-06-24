from library_item import I

class B(I):
    def __init__(self, i, t, a):
        super().__init__(i, t)
        self.a = a

    def d(self):
        return f"Book: {self.t}, Author: {self.a}"
