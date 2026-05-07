Tugas Akhir Percobaan 3

Judul Program : Pencarian Nilai Siswa

Program ini berfungsi untuk mencari dan menghitung berapa kali sebuah nilai muncul dalam daftar nilai siswa. Cara kerjanya cukup sederhana, program ini memeriksa data satu per satu dari awal hingga akhir, mirip seperti seseorang yang sedang mencari nama dalam daftar absen kelas. Apabila nilai yang dicari ditemukan maka akan langsung dihitung, apabila tidak maka program akan melanjutkan ke data berikutnya. Konsep seperti ini sebenarnya sangat bermanfaat dalam kehidupan sehari-hari, misalnya seorang guru dapat langsung mengetahui berapa siswa yang perlu mengikuti remedial tanpa perlu menghitung secara manual, toko online dapat memeriksa berapa kali suatu produk terjual, bahkan rumah sakit pun menggunakan logika yang sama untuk mencari data pasien. Oleh karena itu, meskipun terlihat sederhana, program ini merupakan dasar dari sistem pencarian data yang digunakan setiap hari dalam berbagai teknologi modern.


<img width="1402" height="1394" alt="code3" src="https://github.com/user-attachments/assets/d1eef323-c517-46cb-ac56-17e3aa77b667" />

Penjelasan Code : 

Fungsi sequential_search
Fungsi ini bertugas mencari nilai siswa di dalam daftar secara berurutan satu per satu dari awal sampai akhir. Fungsi ini menerima tiga parameter yaitu data sebagai daftar nilai, n sebagai jumlah data, dan target sebagai nilai yang ingin dicari. Di dalam fungsi terdapat variabel i sebagai penanda posisi dan counter sebagai penghitung, keduanya dimulai dari 0. Setiap kali nilai pada posisi data[i] sama dengan target maka counter akan bertambah 1, begitu terus sampai semua data selesai dicek. Hasil akhir counter dikembalikan ke program utama.

Fungsi main
Fungsi ini adalah program utama yang dijalankan pertama kali. Di sini dibuat daftar nilai siswa berupa angka seperti 75, 85, 90, dan seterusnya, lalu jumlah datanya dihitung otomatis dan ditampilkan ke layar. Setelah itu program meminta pengguna memasukkan nilai yang ingin dicari, jika input bukan angka maka program akan meminta ulang sampai inputnya benar. Setelah input valid diterima, fungsi sequential_search dipanggil untuk mencari nilai tersebut di dalam daftar. Jika nilai ditemukan maka ditampilkan berapa banyak siswa yang mendapat nilai tersebut, dan jika tidak ditemukan maka ditampilkan pesan bahwa nilai tidak ada dalam daftar.


Output Code :
<img width="774" height="66" alt="Cuplikan layar 2026-05-06 154304" src="https://github.com/user-attachments/assets/449a2c5b-4cfd-49df-bbdb-a01f0b96dda7" />



Output Ketika User salah menginputkan data : 
<img width="734" height="67" alt="Cuplikan layar 2026-05-06 154351" src="https://github.com/user-attachments/assets/8a2dd032-a0f2-4f82-9ee0-4c713c5d2786" />

<img width="347" height="40" alt="Cuplikan layar 2026-05-06 180924" src="https://github.com/user-attachments/assets/ae0ba730-209d-4c80-9a2c-e12f1b32ac13" />

Pada output program, tampilan pertama yang muncul adalah daftar nilai siswa yang sudah disimpan di dalam program. Daftar tersebut berisi beberapa nilai siswa yang nantinya akan digunakan dalam proses pencarian data nilai.

Setelah daftar nilai ditampilkan, program meminta pengguna memasukkan nilai yang ingin dicari. Pengguna dapat mengetikkan angka sesuai nilai yang ingin diperiksa di dalam daftar.

Kemudian program menjalankan proses pencarian untuk mengecek apakah nilai tersebut ada di dalam daftar. Jika nilai ditemukan, maka program akan menghitung berapa kali nilai tersebut muncul, lalu menampilkan hasil jumlah siswa yang memiliki nilai tersebut. Contohnya, ketika pengguna memasukkan nilai 75, program menampilkan bahwa nilai 75 ditemukan sebanyak 4 siswa.

Jika nilai yang dimasukkan tidak ada di dalam daftar, maka program akan menampilkan pesan bahwa nilai tersebut tidak ditemukan. Contohnya saat pengguna memasukkan nilai 50, program memberikan informasi bahwa nilai 50 tidak ditemukan.

Selain itu, program juga memiliki validasi input agar pengguna hanya dapat memasukkan angka. Jika pengguna memasukkan huruf atau karakter selain angka, seperti “abc”, maka program akan menampilkan pesan kesalahan berupa “Input tidak valid, silakan masukkan angka!”. Hal ini bertujuan agar program dapat berjalan dengan aman tanpa terjadi error saat proses pencarian data dilakukan.



Link YouTube : https://youtu.be/cFlNvvN9isA?si=GIysVwi9ox-zzzV7
