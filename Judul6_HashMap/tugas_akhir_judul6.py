class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True

            prev = current
            current = current.next

        return False

    def display(self):
        print("\nIsi Lemari Baju:")
        for i in range(self.SIZE):
            print(f"Sekat {i}: ", end="")

            current = self.table[i]

            while current is not None:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next

            print("NULL")


def main():

    lemari = HashMapSeparateChaining()

    print("=== PENYIMPANAN BAJU MENGGUNAKAN HASH MAP ===")

    lemari.insert(1, "Kaos Merah")
    lemari.insert(11, "Kemeja Merah")
    lemari.insert(21, "Jaket Merah")
    lemari.insert(2, "Kaos Biru")

    print("\nSetelah menambahkan baju:")
    lemari.display()

    print("\nMencari Kemeja Merah (kode 11)...")

    hasil = lemari.search(11)

    if hasil is not None:
        print("Baju ditemukan :", hasil.value)
    else:
        print("Baju tidak ditemukan")

    print("\nMenghapus Kemeja Merah (kode 11)...")
    lemari.remove_key(11)

    print("\nIsi lemari setelah penghapusan:")
    lemari.display()


if __name__ == "__main__":
    main()
