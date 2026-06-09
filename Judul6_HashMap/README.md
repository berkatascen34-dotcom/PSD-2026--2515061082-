


Program ini dibuat untuk mensimulasikan sebuah lemari baju digital yang dapat menyimpan, menampilkan, dan mencari data baju berdasarkan kode yang telah ditentukan. Setiap baju yang dimasukkan akan secara otomatis ditempatkan ke dalam sekat yang sesuai menggunakan perhitungan hash, sehingga proses pencarian menjadi lebih cepat dan terorganisir. Program ini juga mampu menangani kondisi di mana dua atau lebih baju memiliki hasil hash yang sama dengan menggunakan teknik Separate Chaining, yaitu menyusun baju-baju tersebut seperti rantai di dalam satu sekat sehingga tidak ada data yang hilang atau tertimpa. Selain itu, program ini juga memungkinkan pengguna untuk berinteraksi langsung dengan cara memasukkan kode baju yang ingin dicari, kemudian program akan menampilkan nama baju tersebut jika ditemukan atau memberikan pemberitahuan jika baju tidak ada di dalam lemari.

---
---

<img width="1402" height="4206" alt="ta 6 code" src="https://github.com/user-attachments/assets/44cf243b-8a6e-4a57-96b0-f5c2fe47daec" />

---
---

Penjelasan Codingan

Class Node


class Node: Membuat "cetakan" untuk setiap baju yang akan disimpan.

def init(self, key, value): Fungsi yang otomatis jalan saat baju baru dibuat. Menerima key (kode baju) dan value (nama baju).

self.key = key Menyimpan kode baju ke dalam objek ini. Contoh: 1, 11, 21.

self.value = value Menyimpan nama bajunya. Contoh: "Kaos Merah".

self.next = None Penunjuk ke baju berikutnya di sekat yang sama. Awalnya kosong karena belum ada baju lain.

---

Class HashMapSeparateChaining

class HashMapSeparateChaining: Membuat "cetakan" untuk lemari bajunya sendiri.

def init(self, size=10):  Fungsi inisialisasi lemari. Defaultnya punya 10 sekat.

self.SIZE = size Menyimpan jumlah sekat lemari (10).

self.table = [None] * self.SIZE Membuat 10 sekat kosong sekaligus. Ibarat lemari dengan 10 laci yang semuanya masih kosong.

---

Fungsi hash_function

def hash_function(self, key): Fungsi untuk menentukan baju ini harus masuk ke sekat nomor berapa.

(key % self.SIZE + self.SIZE) % self.SIZE Menghitung nomor sekat pakai rumus matematika. Contoh: kode 11 → (11 % 10 + 10) % 10 = sekat 1. Rumus ini juga aman untuk angka negatif.

---

Fungsi insert

def insert(self, key, value): Fungsi untuk memasukkan baju ke dalam lemari.

index = self.hash_function(key) Cari dulu baju ini harus masuk ke sekat nomor berapa.

current = self.table[index] Intip isi sekat tersebut, simpan ke variabel current.

while current is not None: Selama sekat belum kosong, telusuri isinya satu per satu.

if current.key == key: Kalau ketemu baju dengan kode yang sama...

current.value = value dan return ...update saja namanya, lalu keluar dari fungsi. Tidak perlu tambah baju baru.

current = current.next Kalau kodenya tidak sama, lanjut cek baju berikutnya di rantai.

new_node = Node(key, value) Kalau tidak ada yang sama, buat objek baju baru dengan kode dan nama yang diberikan.

new_node.next = self.table[index] Baju baru diikat ke depan baju yang sudah ada di sekat tersebut.

self.table[index] = new_node Baju baru dijadikan yang paling depan di sekat itu.

---

Fungsi search

def search(self, key): Fungsi untuk mencari baju berdasarkan kodenya.

index = self.hash_function(key) Hitung sekat yang dituju berdasarkan kode yang dicari.

current = self.table[index] Intip isi sekat tersebut.

while current is not None: Telusuri satu per satu selama isi sekat belum habis.

if current.key == key: dan return current Kalau kodenya cocok, kembalikan data bajunya.

current = current.next Kalau belum cocok, lanjut ke baju berikutnya di rantai.

return None Kalau sudah habis ditelusuri tapi tidak ketemu, kembalikan None artinya baju tidak ada.

---

Fungsi display

def display(self): Fungsi untuk menampilkan semua isi lemari.

print("\nIsi Lemari Baju:") Cetak judul tampilan.

for i in range(self.SIZE): Looping dari sekat 0 sampai 9.

print(f"{i}: ", end="") Cetak nomor sekatnya di setiap baris.

current = self.table[i] Ambil isi sekat tersebut.

while current is not None: Telusuri semua baju di sekat itu satu per satu.

print(f"({current.key}, {current.value}) -> ", end="") Tampilkan baju dalam format (kode, nama) diikuti tanda panah.

current = current.next Lanjut ke baju berikutnya di rantai.

print("NULL") Di akhir setiap sekat, cetak NULL sebagai penanda rantai sudah habis.

---

Fungsi main

hashmap = HashMapSeparateChaining() Buat objek lemari baru dengan 10 sekat.

hashmap.insert(1, "Kaos Merah") sampai hashmap.insert(2, "Kaos Biru") Masukkan 4 baju ke dalam lemari. Perlu diperhatikan bahwa kode 1, 11, dan 21 semuanya masuk ke sekat 1 karena hasil hash-nya sama. Inilah yang disebut collision dan diselesaikan dengan chaining (rantai).

hashmap.display() Tampilkan seluruh isi lemari setelah semua baju dimasukkan.

kode_baju = int(input("\nMasukkan kode baju: ")) Meminta pengguna mengetik kode baju yang ingin dicari, lalu diubah menjadi angka bulat.

hasil = hashmap.search(kode_baju) Cari baju berdasarkan kode yang dimasukkan pengguna.

if hasil is not None: Kalau baju ditemukan, tampilkan nama bajunya lengkap dengan kodenya.

else: dan print("Baju tidak ditemukan") Kalau tidak ditemukan, tampilkan pesan bahwa baju tidak ada.

---

Baris Terakhir

if name == "main": dan main() Pengaman program. Fungsi main hanya dijalankan kalau file ini dieksekusi langsung, bukan ketika dipanggil dari file lain.

---
---

Output

Penjelasan Output

Pada saat program dijalankan, tampilan pertama yang muncul adalah judul Isi Lemari Baju yang berisi data baju yang telah disimpan ke dalam sistem menggunakan metode Hash Map Separate Chaining. Program secara otomatis menambahkan beberapa data baju, yaitu Kaos Merah, Kemeja Merah, Jaket Merah, dan Kaos Biru ke dalam hash table. Setelah itu, seluruh data yang tersimpan akan ditampilkan sesuai dengan posisi sekat hasil perhitungan fungsi hash.

Selanjutnya, pengguna diminta memasukkan kode baju yang ingin dicari. Program akan menggunakan fungsi search() untuk mencari data baju berdasarkan kode yang dimasukkan. Proses pencarian dilakukan dengan langsung menuju sekat yang sesuai, kemudian menelusuri rantai data (chaining) apabila terdapat lebih dari satu baju pada sekat yang sama akibat terjadinya collision.

Jika kode baju ditemukan, program akan menampilkan nama baju yang sesuai dengan kode tersebut. Namun, jika kode yang dimasukkan tidak terdapat di dalam sistem, program akan menampilkan pesan bahwa baju tidak ditemukan. Setelah hasil pencarian ditampilkan, program selesai dijalankan.
