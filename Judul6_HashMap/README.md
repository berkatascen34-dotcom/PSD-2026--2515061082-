


Program ini berfungsi untuk mengelola data baju menggunakan struktur data Hash Map dengan metode Separate Chaining. Setiap baju disimpan menggunakan kode sebagai key dan nama baju sebagai value. Fungsi insert() digunakan untuk menambahkan baju ke dalam lemari, search() digunakan untuk mencari baju berdasarkan kode yang dimasukkan, remove_key() digunakan untuk menghapus data baju, dan display() digunakan untuk menampilkan seluruh isi lemari. Jika terdapat beberapa baju yang memiliki hasil hash yang sama sehingga masuk ke sekat yang sama (collision), program akan menyimpannya dalam bentuk rantai (chaining) sehingga semua data tetap tersimpan dengan baik. Dengan menggunakan Hash Map, proses penyimpanan, pencarian, dan penghapusan data dapat dilakukan dengan lebih cepat dan efisien dibandingkan mencari data satu per satu dari seluruh isi lemari.

---

<img width="1402" height="4206" alt="ta 6 code" src="https://github.com/user-attachments/assets/44cf243b-8a6e-4a57-96b0-f5c2fe47daec" />

---
Penjelasan Codungan

Class Node

class Node: — Membuat "cetakan" untuk setiap baju yang akan disimpan.


def init(self, key, value): — Fungsi yang otomatis jalan saat baju baru dibuat. Menerima key (kode baju) dan value (nama baju).


self.key = key — Menyimpan kode baju ke dalam objek ini. Contoh: 1, 11, 21.


self.value = value — Menyimpan nama bajunya. Contoh: "Kaos Merah".


self.next = None — Penunjuk ke baju berikutnya di sekat yang sama. Awalnya kosong karena belum ada baju lain.

---

Class HashMapSeparateChaining

class HashMapSeparateChaining: — Membuat "cetakan" untuk lemari bajunya sendiri.


def init(self, size=10): — Fungsi inisialisasi lemari. Defaultnya punya 10 sekat.


self.SIZE = size — Menyimpan jumlah sekat lemari (10).


self.table = [None] * self.SIZE — Membuat 10 sekat kosong. Ibarat lemari dengan 10 laci, semuanya masih kosong.

---

Fungsi hash_function

def hash_function(self, key): — Fungsi untuk menentukan baju ini masuk sekat nomor berapa.


(key % self.SIZE + self.SIZE) % self.SIZE — Menghitung nomor sekat pakai rumus matematika. Contoh: kode 11 → (11 % 10 + 10) % 10 = sekat 1. Rumus ini juga aman untuk angka negatif.

---

Fungsi insert

def insert(self, key, value): — Fungsi untuk memasukkan baju ke dalam lemari.


index = self.hash_function(key) — Cari dulu baju ini harus masuk ke sekat nomor berapa.


current = self.table[index] — Intip isi sekat tersebut, simpan ke variabel current.


while current is not None: — Selama sekat belum kosong, telusuri satu per satu.


if current.key == key: — Kalau ketemu baju dengan kode yang sama...


current.value = value dan return — ...update saja namanya, lalu keluar dari fungsi. Tidak perlu tambah baju baru.


current = current.next — Kalau bukan, lanjut cek baju berikutnya di rantai.


new_node = Node(key, value) — Buat objek baju baru dengan kode dan nama yang diberikan.


new_node.next = self.table[index] — Baju baru ini diikat ke depan baju yang sudah ada di sekat tersebut.


self.table[index] = new_node — Baju baru dijadikan yang paling depan di sekat itu.

---

Fungsi search

def search(self, key): — Fungsi untuk mencari baju berdasarkan kodenya.


index = self.hash_function(key) — Hitung sekat yang dituju.


current = self.table[index] — Intip isi sekat tersebut.


while current is not None: — Telusuri satu per satu selama sekat belum habis.


if current.key == key: dan return current — Kalau ketemu kodenya, kembalikan bajunya.


current = current.next — Kalau belum ketemu, lanjut ke baju berikutnya.


return None — Kalau sudah habis ditelusuri tapi tidak ketemu, kembalikan None artinya baju tidak ada.

---

Fungsi remove_key

def remove_key(self, key): — Fungsi untuk menghapus baju dari lemari.


index = self.hash_function(key) — Cari sekat yang dituju.


current = self.table[index] — Simpan baju yang sedang dicek ke variabel current.


prev = None — Simpan baju sebelumnya ke variabel prev, awalnya kosong.


while current is not None: — Telusuri sampai ketemu baju yang kodenya cocok.


if current.key == key: — Kalau kodenya cocok, siap dihapus.


if prev is None: dan self.table[index] = current.next — Kalau baju yang dihapus ada di posisi paling depan, baju berikutnya langsung jadi yang terdepan.


else: dan prev.next = current.next — Kalau baju yang dihapus ada di tengah atau akhir rantai, baju sebelumnya langsung melompati baju yang dihapus.


return True — Penghapusan berhasil, kembalikan True.


prev = current dan current = current.next — Kalau belum ketemu, geser prev dan current ke baju berikutnya.


return False — Kalau tidak ketemu sama sekali, kembalikan False.

---

Fungsi display

def display(self): — Fungsi untuk menampilkan semua isi lemari.


print("\nIsi Lemari Baju:") — Cetak judul tampilan.


for i in range(self.SIZE): — Looping dari sekat 0 sampai 9.


print(f"Sekat {i}: ", end="") — Cetak nomor sekatnya di setiap baris.


current = self.table[i] — Ambil isi sekat tersebut.


while current is not None: — Telusuri semua baju di sekat itu.


print(f"({current.key}, {current.value}) -> ", end="") — Tampilkan baju satu per satu dalam format (kode, nama).


current = current.next — Lanjut ke baju berikutnya di rantai.


print("NULL") — Di akhir setiap sekat, cetak NULL sebagai penanda rantai sudah habis.

---

Fungsi main

lemari = HashMapSeparateChaining() — Buat objek lemari baru dengan 10 sekat.


lemari.insert(1, "Kaos Merah") sampai lemari.insert(2, "Kaos Biru") — Masukkan 4 baju ke lemari. Kode 1, 11, dan 21 semuanya masuk ke sekat 1 karena hasil hash-nya sama. Inilah yang disebut collision dan diselesaikan dengan chaining.


hasil = lemari.search(11) — Cari baju dengan kode 11.


if hasil is not None: — Kalau baju ditemukan, tampilkan namanya. Kalau tidak, cetak pesan baju tidak ditemukan.


lemari.remove_key(11) — Hapus baju dengan kode 11 dari lemari.


lemari.display() — Tampilkan isi lemari setelah penghapusan.

---

Baris Terakhir

if name == "main": dan main() — Pengaman program. Fungsi main hanya dijalankan kalau file ini dieksekusi langsung, bukan ketika dipanggil dari file lain
