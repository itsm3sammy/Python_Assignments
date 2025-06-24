from abc import ABC, abstractmethod

class B:
    def __init__(self, i, t, a):
        self.__i = i
        self.__t = t
        self.__a = a

    @property
    def id(self):
        return self.__i

    @property
    def title(self):
        return self.__t

    @property
    def author(self):
        return self.__a

    @property
    def set_id(self):
        return self.__i

    @property
    def set_title(self):
        return self.__t

    @property
    def set_author(self):
        return self.__a


class L(ABC):
    def __init__(self):
        self.b = {}
        self.m

    @abstractmethod
    def add(self, x):
        if x.id in self.b:
            print("Book already exists")
        else:
            self.b[x.id] = x
            print(f"Book '{x.title}' added to the library.")

    @abstractmethod
    def rem(self, i):
        if i in self.b:
            r = self.b.pop(i)
            print(f"Book {r} has been removed from library")
        else:
            print("Book not found")

    def reg(self, m):
        if m.person_id in self.m:
            print("Member already registered.")
        else:
            self.m[m.person_id] = m
            print(f"Member '{m.name}' registered.")

    @property
    def get(self, i):
        return self.b.get(i, None)

    def get_m(self, i):
        return self.m.get(i, None)

    def show_b(self):
        if not self.b:
            print("No books in the library.")
        else:
            for x in self.b.values():
                print(x)

    def show_m(self):
        if not self.m:
            print("No members registered.")
        else:
            for x in self.m.values():
                print(f"{x.person_id}: {x.name}")
