Tugas Akhir Percobaan 2

Judul Program : Pencarian Nilai Siswa

Program ini berfungsi untuk mencari dan menghitung berapa kali sebuah nilai muncul dalam daftar nilai siswa. Cara kerjanya cukup sederhana, program ini memeriksa data satu per satu dari awal hingga akhir, mirip seperti seseorang yang sedang mencari nama dalam daftar absen kelas. Apabila nilai yang dicari ditemukan maka akan langsung dihitung, apabila tidak maka program akan melanjutkan ke data berikutnya. Konsep seperti ini sebenarnya sangat bermanfaat dalam kehidupan sehari-hari, misalnya seorang guru dapat langsung mengetahui berapa siswa yang perlu mengikuti remedial tanpa perlu menghitung secara manual, toko online dapat memeriksa berapa kali suatu produk terjual, bahkan rumah sakit pun menggunakan logika yang sama untuk mencari data pasien. Oleh karena itu, meskipun terlihat sederhana, program ini merupakan dasar dari sistem pencarian data yang digunakan setiap hari dalam berbagai teknologi modern.


<img width="1402" height="1394" alt="code3" src="https://github.com/user-attachments/assets/d1eef323-c517-46cb-ac56-17e3aa77b667" />

Penjelasan Code : 

Fungsi sequential_search
Fungsi ini menggunakan konsep iterasi yaitu perulangan while yang berjalan selama kondisi i < n bernilai True. 

Variabel i bertipe integer yang berfungsi sebagai index untuk mengakses elemen list satu per satu menggunakan data[i]. 

Variabel counter juga bertipe integer yang nilainya bertambah menggunakan operator += setiap kali kondisi if terpenuhi. 

Method .lower() bertipe string digunakan pada kedua sisi perbandingan agar pencarian bersifat case-insensitive, dan operator in digunakan untuk mengecek apakah substring target ada di dalam data[i]. 

Di akhir fungsi, keyword return mengembalikan nilai counter ke pemanggil fungsi.

Fungsi main
Variabel data bertipe list of string yang menyimpan kumpulan nama barang. 

Fungsi bawaan len() digunakan untuk mendapatkan panjang list secara otomatis dan disimpan ke variabel n. 

Blok while True dikombinasikan dengan try-except untuk menangani exception handling, dimana raise ValueError dipanggil secara manual ketika input kosong terdeteksi melalui method .strip(). 

Keyword break digunakan untuk keluar dari perulangan saat input valid diterima. 

Fungsi sequential_search kemudian dipanggil dengan passing argument data, n, dan target, lalu hasilnya disimpan ke variabel counter. 

Terakhir, struktur if-else digunakan untuk menentukan output yang ditampilkan menggunakan f-string ke layar.

