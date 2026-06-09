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

    def display(self):
        print("\nIsi Lemari Baju:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]

            while current is not None:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next

            print("NULL")


def main():
    hashmap = HashMapSeparateChaining()

    hashmap.insert(1, "Kaos Merah")
    hashmap.insert(11, "Kemeja Merah")
    hashmap.insert(21, "Jaket Merah")
    hashmap.insert(2, "Kaos Biru")

    hashmap.display()

    kode_baju = int(input("\nMasukkan kode baju: "))

    hasil = hashmap.search(kode_baju)

    if hasil is not None:
        print(f"Nama baju dengan kode {kode_baju}: {hasil.value}")
    else:
        print("Baju tidak ditemukan")


if __name__ == "__main__":
    main()
