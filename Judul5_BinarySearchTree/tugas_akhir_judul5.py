class Node:
    def __init__(self, nomor):
        self.key = nomor
        self.left = None
        self.right = None


class AntreanBengkel:
    def __init__(self):
        self.root = None

    def tambah_antrean(self, root, nomor):
        if root is None:
            return Node(nomor)

        if nomor < root.key:
            root.left = self.tambah_antrean(root.left, nomor)
        elif nomor > root.key:
            root.right = self.tambah_antrean(root.right, nomor)

        return root

    def insert(self, nomor):
        self.root = self.tambah_antrean(self.root, nomor)

    def cari_antrean_terkecil(self, root):
        current = root

        while current is not None and current.left is not None:
            current = current.left

        return current

    def hapus_antrean(self, root, nomor):
        if root is None:
            return None

        if nomor < root.key:
            root.left = self.hapus_antrean(root.left, nomor)

        elif nomor > root.key:
            root.right = self.hapus_antrean(root.right, nomor)

        else:
            if root.left is None and root.right is None:
                return None

            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            else:
                pengganti = self.cari_antrean_terkecil(root.right)
                root.key = pengganti.key
                root.right = self.hapus_antrean(root.right, pengganti.key)

        return root

    def delete(self, nomor):
        self.root = self.hapus_antrean(self.root, nomor)

    def jumlah_level(self, root):
        if root is None:
            return -1

        kiri = self.jumlah_level(root.left)
        kanan = self.jumlah_level(root.right)

        return 1 + max(kiri, kanan)

    def tampilkan_antrean(self, root):
        if root is None:
            print("(Tidak ada antrean)")
            return

        queue = []
        queue.append(root)

        while len(queue) > 0:
            current = queue.pop(0)

            print(current.key, end=" ")

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        print()

    def antrean_berikutnya(self, root, nomor):
        current = root
        successor = None

        while current is not None:
            if nomor < current.key:
                successor = current
                current = current.left

            elif nomor > current.key:
                current = current.right

            else:
                break

        if current is None:
            return None, False

        if current.right is not None:
            successor = self.cari_antrean_terkecil(current.right)

        if successor is None:
            return None, False

        return successor.key, True

    def antrean_sebelumnya(self, root, nomor):
        current = root
        predecessor = None

        while current is not None:
            if nomor > current.key:
                predecessor = current
                current = current.right

            elif nomor < current.key:
                current = current.left

            else:
                break

        if current is None:
            return None, False

        if current.left is not None:
            temp = current.left

            while temp.right is not None:
                temp = temp.right

            predecessor = temp

        if predecessor is None:
            return None, False

        return predecessor.key, True


def main():
    bengkel = AntreanBengkel()
    pilih = 0

    while pilih != 7:
        print("\n=== SISTEM ANTREAN BENGKEL ===")
        print("1. Tambah Antrean Kendaraan")
        print("2. Kendaraan Selesai Service")
        print("3. Tampilkan Antrean")
        print("4. Lihat Tingkat Antrean")
        print("5. Cari Antrean Berikutnya")
        print("6. Cari Antrean Sebelumnya")
        print("7. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                nomor = int(input("Masukkan nomor antrean: "))
                bengkel.insert(nomor)
                print(f"Nomor antrean {nomor} berhasil ditambahkan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                nomor = int(input("Nomor antrean selesai service: "))
                bengkel.delete(nomor)
                print(f"Nomor antrean {nomor} telah dihapus")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            print("Daftar antrean: ", end="")
            bengkel.tampilkan_antrean(bengkel.root)

        elif pilih == 4:
            print(f"Tingkat antrean saat ini: {bengkel.jumlah_level(bengkel.root)}")

        elif pilih == 5:
            try:
                nomor = int(input("Cari antrean setelah nomor: "))
                hasil, ditemukan = bengkel.antrean_berikutnya(bengkel.root, nomor)

                if ditemukan:
                    print(f"Antrean berikutnya adalah {hasil}")
                else:
                    print("Tidak ada antrean berikutnya")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 6:
            try:
                nomor = int(input("Cari antrean sebelum nomor: "))
                hasil, ditemukan = bengkel.antrean_sebelumnya(bengkel.root, nomor)

                if ditemukan:
                    print(f"Antrean sebelumnya adalah {hasil}")
                else:
                    print("Tidak ada antrean sebelumnya")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 7:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
