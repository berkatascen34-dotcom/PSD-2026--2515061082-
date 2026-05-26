Tugas Akhir Percobaan 5 

Judul Program : Sistem Antrean Kendaraan

Program **Sistem Antrean Bengkel** ini digunakan untuk membantu mengelola nomor antrean kendaraan yang akan melakukan servis di bengkel. Program bekerja dengan menyimpan nomor antrean ke dalam struktur data Binary Search Tree (BST) sehingga data dapat disimpan dan dikelola dengan lebih teratur. Pengguna dapat menambahkan nomor antrean kendaraan yang baru datang, menghapus nomor antrean kendaraan yang sudah selesai servis, serta melihat seluruh daftar antrean yang masih menunggu. Selain itu, program juga dapat menampilkan tingkat atau tinggi antrean yang tersimpan, mencari nomor antrean berikutnya setelah suatu nomor tertentu, dan mencari nomor antrean sebelumnya. Dengan adanya fitur-fitur tersebut, proses pengelolaan antrean menjadi lebih mudah, cepat, dan terorganisir sehingga petugas bengkel dapat mengetahui urutan kendaraan yang sedang menunggu maupun yang akan dilayani berikutnya.

<img width="792" height="878" alt="Cuplikan layar 2026-05-26 174209" src="https://github.com/user-attachments/assets/3964674a-fdff-4b56-83dc-5383b3531616" />
<img width="806" height="801" alt="Cuplikan layar 2026-05-26 174240" src="https://github.com/user-attachments/assets/fc11ad29-f31d-4974-b024-525f5c2b3cd7" />
<img width="796" height="811" alt="Cuplikan layar 2026-05-26 174310" src="https://github.com/user-attachments/assets/5cd65476-405b-432e-8185-3cac5d1300d4" />
<img width="793" height="809" alt="Cuplikan layar 2026-05-26 174340" src="https://github.com/user-attachments/assets/4f94baa8-7d03-4395-991e-4cce66763305" />
<img width="812" height="824" alt="Cuplikan layar 2026-05-26 174406" src="https://github.com/user-attachments/assets/fcedc723-cffc-4332-93f2-98f98e47a35c" />
<img width="897" height="845" alt="Cuplikan layar 2026-05-26 174426" src="https://github.com/user-attachments/assets/38195b94-dd45-4a41-ab4a-ce95fa2a141a" />
<img width="804" height="121" alt="Cuplikan layar 2026-05-26 174440" src="https://github.com/user-attachments/assets/421cd587-3ccf-41e9-9e49-54da003e5116" />


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

