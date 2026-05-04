Tugas Akhir Percobaan 2

Judul Program : Pengurutan Barisan Siswa Berdasarkan Tinggi Badan Dari Terpendek ke Tertinggi 


Program ini digunakan untuk membantu mengurutkan data tinggi badan siswa secara otomatis dari yang paling pendek hingga yang paling tinggi, sehingga pengguna tidak perlu melakukan pengurutan secara manual yang dapat memakan waktu dan berpotensi menimbulkan kesalahan. Program menerima input berupa jumlah siswa dan tinggi badan masing-masing, kemudian memanfaatkan metode Bubble Sort untuk membandingkan data yang bersebelahan dan menukarnya jika urutannya belum sesuai. Proses ini dilakukan secara berulang hingga seluruh data tersusun dengan benar. Dengan demikian, data yang awalnya acak dapat diubah menjadi urutan yang rapi, sehingga memudahkan dalam melihat perbedaan tinggi antar siswa, menentukan urutan barisan, atau keperluan lain seperti pembagian kelompok berdasarkan tinggi badan secara cepat, tepat, dan terstruktur.


<img width="1480" height="2002" alt="Judul 2 sorting1" src="https://github.com/user-attachments/assets/6bd1676e-537e-4ea3-8d26-54ff9f267627" />



Penjelasan Code : 
1. Fungsi tukar() — Si Penukar Posisi
Fungsi ini tugasnya hanya satu: menukar posisi dua angka dalam daftar. Analoginya seperti menukar isi dua gelas air — kamu butuh gelas ketiga (variabel sementara) untuk menampung salah satu isi dulu, baru bisa ditukar. Tanpa gelas ketiga itu, salah satu nilai akan tertimpa dan hilang.

2. Fungsi bubble_sort() — Metode Gelembung
Ini adalah inti dari program, yaitu cara mengurutkan semua data. Cara kerjanya seperti siswa yang berbaris: dua orang yang berdampingan saling membandingkan tinggi, kalau yang kiri lebih tinggi dari yang kanan, mereka bertukar tempat. Proses ini diulang terus dari awal sampai semua sudah urut dari pendek ke tinggi. Nama "bubble" (gelembung) karena angka terbesar akan terus bergeser ke posisi paling akhir setiap putaran, seperti gelembung udara naik ke permukaan air.

3. Fungsi main() — Bagian Utama Program
Ini bagian yang langsung berinteraksi dengan pengguna, dan ada tiga langkah di dalamnya:

      Langkah 1 – Tanya jumlah siswa. Program bertanya berapa siswa yang mau diinput. Kalau pengguna salah ketik (misalnya huruf bukan angka), program langsung bilang "Input tidak valid!" dan berhenti.

      Langkah 2 – Input tinggi badan satu per satu. Program meminta tinggi badan setiap siswa. Kalau salah input, program tidak langsung berhenti — ia minta coba lagi sampai benar.

      Langkah 3 – Tampilkan hasilnya. Program menampilkan data sebelum diurutkan, lalu menjalankan bubble sort, lalu menampilkan hasil akhirnya.



Output Code:
<img width="1919" height="1027" alt="Cuplikan layar 2026-05-02 203203" src="https://github.com/user-attachments/assets/a9ed7408-5e76-4c23-b919-08b30b65c129" />

Output Code Ketika Salah Dalam Mengimputkan 
<img width="260" height="47" alt="Cuplikan layar 2026-05-04 185544" src="https://github.com/user-attachments/assets/a64b7898-ed96-4f44-93f7-60e97176fa5a" />




<img width="304" height="128" alt="Cuplikan layar 2026-05-04 185600" src="https://github.com/user-attachments/assets/ce80562b-5dff-4b5b-96b4-4d7f89d65312" />



Link YouTube: [https://youtu.be/TISxt_lZTB8?si=25KT6z3hE6cn-S4R](https://youtu.be/_7RgiM3VQsM?si=M6NZIIBrF7tVuitI)
