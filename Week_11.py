from abc import ABC, abstractmethod

class V(ABC):
    @abstractmethod
    def cost(self, d):
        pass

    @abstractmethod
    def lic(self):
        pass

    def info(self):
        print("This is a vehicle available for rental")

class C(V):
    def cost(self, d):
        return 100 * d

    def lic(self):
        return "Standard Car License"

    def info(self):
        super().info()
        print("This is a sedan car suitable for families")
        print("Rental cost for 3 days:", self.cost(3))
        print("License required:", self.lic())
        print("-" * 40)

class B(V):
    def cost(self, d):
        return 50 * d

    def lic(self):
        return "Two-Wheeler License"

    def info(self):
        super().info()
        print("This is a bullet bike suitable for solo ride")
        print("Rental cost for 3 days:", self.cost(3))
        print("License required:", self.lic())
        print("-" * 40)

class T(V):
    def cost(self, d):
        return 150 * d

    def lic(self):
        return "Heavy Vehicle License"

    def info(self):
        super().info()
        print("This is a heavy truck suitable for transport")
        print("Rental cost for 3 days:", self.cost(3))
        print("License required:", self.lic())
        print("-" * 40)

def m():
    c = C()
    c.info()

    b = B()
    b.info()

    t = T()
    t.info()

m()
