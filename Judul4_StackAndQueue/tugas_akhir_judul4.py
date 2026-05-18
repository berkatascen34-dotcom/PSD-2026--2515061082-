class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueKendaraan:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None
        self.jumlah = 0
        self.batas = 10

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, kendaraan):
        new_node = Node(kendaraan)

        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node

        self.jumlah += 1

        print(f"Kendaraan {kendaraan} masuk ke antrean.")

        if self.jumlah >= self.batas:
            print("PERINGATAN: Antrean padat!")
        else:
            print("Antrean lancar dan aman.")

    def dequeue(self):
        if self.is_empty():
            print("Antrean kosong.")
            return

        temp = self.front_ptr
        print(f"Kendaraan {temp.data} keluar dari antrean.")

        self.front_ptr = self.front_ptr.next

        if self.front_ptr is None:
            self.rear_ptr = None

        self.jumlah -= 1

    def peek(self):
        if self.is_empty():
            print("Antrean kosong.")
            return

        print(f"Kendaraan paling depan: {self.front_ptr.data}")

    def display(self):
        if self.is_empty():
            print("Antrean kosong.")
            return

        print("Daftar antrean kendaraan:")

        current = self.front_ptr
        while current is not None:
            print("-", current.data)
            current = current.next

        print(f"Jumlah kendaraan dalam antrean: {self.jumlah}")

        if self.jumlah >= self.batas:
            print("Status: Antrean padat!")
        else:
            print("Status: Antrean lancar dan aman.")


def main():
    antrean = QueueKendaraan()
    pilih = 0

    while pilih != 5:
        print("\n=== SISTEM ANTREAN KENDARAAN ===")
        print("1. Tambah kendaraan")
        print("2. Keluarkan kendaraan")
        print("3. Lihat kendaraan terdepan")
        print("4. Tampilkan antrean")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            nama = input("Masukkan nomor/nama kendaraan: ")
            antrean.enqueue(nama)

        elif pilih == 2:
            antrean.dequeue()

        elif pilih == 3:
            antrean.peek()

        elif pilih == 4:
            antrean.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak tersedia!")


if __name__ == "__main__":
    main()
