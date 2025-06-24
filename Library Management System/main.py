from book import B
from magazine import G
from library_member import M
from labrary import L

def main():
    # Create library
    l = L()

    # Create items
    b1 = B("B001", "1984", "George Orwell")
    b2 = B("B002", "Sapiens", "Yuval Noah Harari")
    g1 = G("M001", "TIME", "2024-06", "Time Inc.")
    g2 = G("M002", "NatGeo", "2024-05", "National Geographic")

    # Add items to library
    l.add(b1)
    l.add(b2)
    l.add(g1)
    l.add(g2)

    # Create members
    m1 = M("U001", "Alice")
    m2 = M("U002", "Bob")

    # Register members
    l.reg(m1)
    l.reg(m2)

    # Borrow and return
    m1.br(b1)
    m1.br(g2)
    m2.br(b2)

    # Display borrowed items
    print(f"{m1.n} has borrowed:", ", ".join(m1.d()))
    print(f"{m2.n} has borrowed:", ", ".join(m2.d()))

    # Return an item
    m1.rt(b1)
    print(f"\nAfter returning a book, {m1.n} has borrowed:", ", ".join(m1.d()))

    # Display item details
    print("\nItem Details:")
    print(b1.d())
    print(b2.d())
    print(g1.d())
    print(g2.d())

if __name__ == "__main__":
    main()
