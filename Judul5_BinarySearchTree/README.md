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


10. tampilkan_antrean()
Menampilkan seluruh nomor antrean yang tersimpan.
Menggunakan metode Level Order Traversal.
Data ditampilkan dari atas ke bawah dan dari kiri ke kanan.


11. antrean_berikutnya()
Mencari nomor antrean setelah nomor tertentu.
Dalam BST disebut Successor.


12. antrean_sebelumnya()
Mencari nomor antrean sebelum nomor tertentu.
Dalam BST disebut Predecessor.


13. main()
Menjadi pusat jalannya program.
Mengatur menu dan menerima input dari pengguna.


14. Menu 1 - Tambah Antrean Kendaraan
Menambahkan nomor antrean baru ke sistem.
Kendaraan baru akan masuk ke BST.


15. Menu 2 - Kendaraan Selesai Service
Menghapus nomor antrean kendaraan yang sudah selesai.
Data kendaraan akan dihapus dari BST.


16. Menu 3 - Tampilkan Antrean
Menampilkan seluruh nomor antrean yang masih aktif.


17. Menu 4 - Cari Antrean Berikutnya
Menampilkan kendaraan yang akan dipanggil setelah nomor tertentu.
Analogi: Mengetahui siapa pelanggan berikutnya yang akan masuk ke ruang servis.


18. Menu 5 - Cari Antrean Sebelumnya
Menampilkan kendaraan yang dipanggil sebelum nomor tertentu.
Analogi: Mengetahui pelanggan yang sudah dipanggil tepat sebelum kendaraan tersebut.


19. Menu 6 - Keluar
Mengakhiri program.
Analogi: Petugas menutup sistem antrean karena jam operasional bengkel telah selesai.

---

OutPut

User Mengimputkan Pilihan Menu 1 

<img width="356" height="722" alt="Cuplikan layar 2026-05-26 190507" src="https://github.com/user-attachments/assets/1af4b9d2-8c0a-4e80-8672-fb22b190124b" />
<img width="360" height="725" alt="Cuplikan layar 2026-05-26 190520" src="https://github.com/user-attachments/assets/93c24bda-6c11-4db6-92f2-4217e087ad92" />
<img width="354" height="713" alt="Cuplikan layar 2026-05-26 190537" src="https://github.com/user-attachments/assets/975f99e9-4f7b-4c7f-8da7-8c8c493ce6ad" />
<img width="359" height="241" alt="Cuplikan layar 2026-05-26 190549" src="https://github.com/user-attachments/assets/a7bdd290-d172-42f8-8757-0a10b5ef2bee" />

---

User Mengimputkan Pilhan Menu 3 

<img width="350" height="212" alt="Cuplikan layar 2026-05-26 190608" src="https://github.com/user-attachments/assets/d8e70b7c-d699-4468-aab2-79e826ef393f" />

---

User Mengimputkan Pilihan Menu 4 

<img width="301" height="228" alt="Cuplikan layar 2026-05-26 190631" src="https://github.com/user-attachments/assets/36bf2690-adc2-416d-a884-db99c8d8e873" />

---

User Mengimputkan Pilihan Menu 5 

<img width="284" height="232" alt="Cuplikan layar 2026-05-26 190647" src="https://github.com/user-attachments/assets/af83b30c-21a7-4ee1-be17-dc4b6a9477bf" />

---

User Mau Menghapus Antrian Mobil Yang Telah Di Service Dari Antrean 

<img width="318" height="239" alt="Cuplikan layar 2026-05-26 190700" src="https://github.com/user-attachments/assets/1146a07d-295d-4c44-b36d-55fca1b5e5a5" />

---

User Mau Melihat Kembali Tampilan Antrian Yang Terbaru 

<img width="328" height="211" alt="Cuplikan layar 2026-05-26 190713" src="https://github.com/user-attachments/assets/1a5a9640-311f-4bda-b2d3-24b30c307b57" />

---

Penjelasan OutPut 

Pada output program, tampilan pertama yang muncul adalah judul program, yaitu **Sistem Antrean Bengkel**. Setelah itu, pengguna akan melihat beberapa menu yang dapat dipilih, seperti menambah antrean kendaraan, menghapus antrean kendaraan yang telah selesai servis, menampilkan daftar antrean, melihat tingkat antrean, mencari antrean berikutnya, mencari antrean sebelumnya, dan keluar dari program.

Ketika pengguna memilih menu **Tambah Antrean Kendaraan**, program akan meminta pengguna memasukkan nomor antrean kendaraan. Nomor antrean yang dimasukkan akan disimpan ke dalam struktur data Binary Search Tree (BST). Program juga menggunakan penanganan kesalahan (*exception handling*) sehingga jika pengguna memasukkan data yang bukan angka, program akan menampilkan pesan bahwa input tidak valid dan meminta pengguna mengulangi proses input.

Setelah beberapa nomor antrean berhasil dimasukkan, pengguna dapat memilih menu **Tampilkan Antrean** untuk melihat seluruh nomor antrean yang tersimpan. Data akan ditampilkan menggunakan metode *Level Order Traversal*, yaitu menampilkan node dari level paling atas ke level berikutnya secara berurutan.

Pengguna juga dapat memilih menu **Kendaraan Selesai Service** untuk menghapus nomor antrean tertentu dari sistem. Setelah nomor antrean berhasil dihapus, program akan memperbarui struktur BST secara otomatis agar tetap sesuai dengan aturan Binary Search Tree.

Pada menu **Lihat Tingkat Antrean**, program akan menghitung dan menampilkan tinggi pohon BST yang terbentuk dari data antrean yang telah dimasukkan. Informasi ini menunjukkan jumlah tingkat atau level yang dimiliki oleh struktur pohon saat ini.

Selanjutnya, pada menu **Cari Antrean Berikutnya**, pengguna dapat memasukkan nomor antrean tertentu untuk mengetahui nomor antrean yang akan dipanggil setelah nomor tersebut. Program akan mencari nilai *successor* dari nomor antrean yang dipilih dan menampilkannya kepada pengguna apabila ditemukan.

Pada menu **Cari Antrean Sebelumnya**, pengguna dapat memasukkan nomor antrean tertentu untuk mengetahui nomor antrean yang berada sebelum nomor tersebut. Program akan mencari nilai *predecessor* dan menampilkan hasilnya apabila data ditemukan.

Program akan terus menampilkan menu utama dan menerima perintah dari pengguna sampai pengguna memilih menu **Keluar**. Ketika menu keluar dipilih, program akan menampilkan pesan bahwa program telah selesai dijalankan dan kemudian berhenti.





