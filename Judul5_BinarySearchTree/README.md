Tugas Akhir Percobaan 5 

Judul Program : Sistem Antrean Kendaraan

Program **Sistem Antrean Bengkel** ini digunakan untuk membantu mengelola nomor antrean kendaraan yang akan melakukan servis di bengkel. Program bekerja dengan menyimpan nomor antrean ke dalam struktur data Binary Search Tree (BST) sehingga data dapat disimpan dan dikelola dengan lebih teratur. Pengguna dapat menambahkan nomor antrean kendaraan yang baru datang, menghapus nomor antrean kendaraan yang sudah selesai servis, serta melihat seluruh daftar antrean yang masih menunggu. Selain itu, program juga dapat menampilkan tingkat atau tinggi antrean yang tersimpan, mencari nomor antrean berikutnya setelah suatu nomor tertentu, dan mencari nomor antrean sebelumnya. Dengan adanya fitur-fitur tersebut, proses pengelolaan antrean menjadi lebih mudah, cepat, dan terorganisir sehingga petugas bengkel dapat mengetahui urutan kendaraan yang sedang menunggu maupun yang akan dilayani berikutnya.


<img width="1280" height="1508" alt="judul5 32" src="https://github.com/user-attachments/assets/7c8d9c5d-d50d-403a-9568-085e8944ee31" />
<img width="1448" height="1280" alt="judul5 59" src="https://github.com/user-attachments/assets/dde8fdf7-67c5-4713-9ea7-778fa8c137be" />
<img width="1172" height="1508" alt="judul5 92" src="https://github.com/user-attachments/assets/bf63eb1b-858c-4732-8521-c1192cc27f7f" />
<img width="1310" height="1242" alt="judul5 118" src="https://github.com/user-attachments/assets/73678ddb-2f43-4573-8aff-aec5e7af6aec" />
<img width="956" height="1470" alt="judul5 149" src="https://github.com/user-attachments/assets/b7c2f427-6e83-49ef-8362-84b3b5613f05" />
<img width="1356" height="1318" alt="judul5 178" src="https://github.com/user-attachments/assets/100bdece-a593-44a3-a4fc-3931c3b70a6c" />
<img width="1602" height="1318" alt="judul5 205" src="https://github.com/user-attachments/assets/05c2ecd9-9ac2-4030-82df-9b9ba91cbdc2" />
<img width="1572" height="1090" alt="judul5 227" src="https://github.com/user-attachments/assets/b238d0e6-cc60-49b7-a076-10d9dbdfaac1" />

---

**Penjelasan Code**

1. class Node
Digunakan untuk membuat satu data antrean kendaraan.
Setiap node menyimpan:
Nomor antrean (key)
Data di sebelah kiri (left)
Data di sebelah kanan (right)


2. class AntreanBengkel
Digunakan untuk mengelola seluruh antrean kendaraan.
Berisi semua fungsi yang diperlukan untuk menambah, menghapus, mencari, dan menampilkan antrean.


3. __init__()
self.root = None
Membuat BST dalam keadaan kosong.
root adalah data pertama atau akar dari BST.
Analogi: bengkel baru buka dan belum ada kendaraan yang mengantre.


4. tambah_antrean()
Berfungsi menambahkan nomor antrean ke BST.
Jika posisi kosong, nomor antrean langsung dimasukkan.
Jika nomor lebih kecil, ditempatkan di sebelah kiri.
Jika nomor lebih besar, ditempatkan di sebelah kanan.


6. insert()
def insert(self, nomor):
Digunakan untuk memanggil fungsi tambah antrean.
Menjadi penghubung antara menu dan BST.


7. cari_antrean_terkecil()
Mencari nomor antrean paling kecil dalam BST.
Program akan terus bergerak ke cabang kiri sampai tidak ada lagi cabang kiri.

8. hapus_antrean()
Digunakan untuk menghapus nomor antrean yang sudah selesai servis.
Program mencari nomor antrean yang ingin dihapus.
Setelah ditemukan, BST akan diatur kembali agar tetap terstruktur.


9. delete()
def delete(self, nomor):
Memanggil fungsi hapus antrean.
Digunakan saat pengguna memilih menu kendaraan selesai servis.


10. jumlah_level()
Menghitung tinggi atau kedalaman BST.
Membandingkan tinggi cabang kiri dan kanan.
Mengambil nilai yang paling besar.


11. tampilkan_antrean()
Menampilkan seluruh nomor antrean yang tersimpan.
Menggunakan metode Level Order Traversal.
Data ditampilkan dari atas ke bawah dan dari kiri ke kanan.


12. antrean_berikutnya()
Mencari nomor antrean setelah nomor tertentu.
Dalam BST disebut Successor.


13. antrean_sebelumnya()
Mencari nomor antrean sebelum nomor tertentu.
Dalam BST disebut Predecessor.


14. main()
Menjadi pusat jalannya program.
Mengatur menu dan menerima input dari pengguna.


15. Menu 1 - Tambah Antrean Kendaraan
Menambahkan nomor antrean baru ke sistem.
Kendaraan baru akan masuk ke BST.


16. Menu 2 - Kendaraan Selesai Service
Menghapus nomor antrean kendaraan yang sudah selesai.
Data kendaraan akan dihapus dari BST.


17. Menu 3 - Tampilkan Antrean
Menampilkan seluruh nomor antrean yang masih aktif.


18. Menu 4 - Lihat Tingkat Antrean
Menampilkan tinggi BST.
Analogi: Mengetahui seberapa banyak tingkat antrean yang sudah terbentuk.


19. Menu 5 - Cari Antrean Berikutnya
Menampilkan kendaraan yang akan dipanggil setelah nomor tertentu.
Analogi: Mengetahui siapa pelanggan berikutnya yang akan masuk ke ruang servis.


20. Menu 6 - Cari Antrean Sebelumnya
Menampilkan kendaraan yang dipanggil sebelum nomor tertentu.
Analogi: Mengetahui pelanggan yang sudah dipanggil tepat sebelum kendaraan tersebut.


21. Menu 7 - Keluar
Mengakhiri program.
Analogi: Petugas menutup sistem antrean karena jam operasional bengkel telah selesai.

---

