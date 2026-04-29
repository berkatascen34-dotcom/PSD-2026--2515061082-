Tugas Akhir Percobaan 1

Judul Program : Sistem Penilaian Sekolah 

Program ini berjalan sebagai sistem sederhana untuk mengelola evaluasi di lima disiplin ilmu. Pengguna dapat memasukkan nilai untuk setiap pelajaran menggunakan menu tersedia kemudian, nilai-nilai tersebut disimpan dalam daftar untuk pengambilan kembali di kemudian hari tanpa perlu memamsukkan ulang. Perangkat lunak ini juga menawarkan opsi kepada pengguna untuk menampilkan semua nilai yang telah dimasukkan, sehingga menyederhanakan penilaian umum data. Selain itu, program secara otomatis menentukan nilai rata-rata dan total sebelum memberikan nilai berdasarkan rata-rata tersebut. 
Agoritma dan struktur data yang diterapkan dalam program ini adalah List 1D (satu dimensi). Penggunaan list ini memungkinkan program untuk menyimpan, mengelola, dan mengolah data nilai secara sederhana dan efisien, seperti saaat melakukan input, menampilkan data, hingga menghitung total dan rata-rata nilai.

Source Code : 

<img width="1572" height="2838" alt="code1" src="https://github.com/user-attachments/assets/320b361f-c7bc-485f-9291-00d7a2da8236" />


PENJELASAN CODE 

. Fungsi menu()

  Bertugas menampilkan daftar pilihan menu ke layar
  Isi: 4 pilihan menu yang dicetak dengan print()

. Fungsi main() 

  nilai = [0 for _ in range(5)] → membuat list 5 angka nol sebagai tempat menyimpan nilai
  pelajaran = [...] → menyimpan nama 5 mata pelajaran
  running = True → variabel pengendali loop utama
  while running: → program terus berjalan selama running bernilai True

. Membaca Pilihan Menu

  menu() dipanggil setiap putaran untuk menampilkan pilihan
  try/except ValueError → menangani jika pengguna mengetik bukan angka
  continue → jika input salah, langsung kembali ke awal loop

. Menu 1 — Input Nilai

  Loop for i in range(5) → meminta nilai untuk tiap pelajaran satu per satu
  while True + break → terus meminta input sampai angka yang valid dimasukkan
  nilai[i] = int(input(...)) → menyimpan nilai ke list di posisi yang sesuai

. Menu 2 — Lihat Nilai

  Loop for i in range(5) → menampilkan semua nama pelajaran beserta nilainya
  Menggunakan f-string f"{pelajaran[i]}: {nilai[i]}" untuk format tampilan

. Menu 3 — Rata-rata & Grade

  sum(nilai) → menjumlahkan semua nilai secara otomatis
  total / 5 → menghitung rata-rata
  Rantai if/elif/else → menentukan grade (A/B/C/D/E) berdasarkan range nilai rata-rata

. Menu 4 — Keluar

  running = False → menghentikan loop utama sehingga program selesai

. Entry Point

  if __name__ == "__main__": → memastikan main() hanya dipanggil saat file dijalankan langsung, bukan saat diimpor


OUTPUT MENU
<img width="268" height="111" alt="Cuplikan layar 2026-04-29 145526" src="https://github.com/user-attachments/assets/e684cd9b-89ef-4128-a758-3ef5af2c1683" />
MENU 1
<img width="328" height="169" alt="Cuplikan layar 2026-04-29 145543" src="https://github.com/user-attachments/assets/6fc07e0f-7abe-4547-86e2-3a706bef5d29" />

MENU 2 sebelum diinputkan nilai
<img width="189" height="132" alt="Cuplikan layar 2026-04-29 150028" src="https://github.com/user-attachments/assets/c9dd2b5f-e97b-4ec2-ba61-decc43e42915" />
Setelah di inputkan nilai 
<img width="188" height="174" alt="Cuplikan layar 2026-04-29 145603" src="https://github.com/user-attachments/assets/3925b1d2-14da-4a86-b442-a926d3353d09" />

MENU 3 
<img width="184" height="131" alt="Cuplikan layar 2026-04-29 150147" src="https://github.com/user-attachments/assets/2de9186d-9fba-4ea6-b201-0ac194ee08c1" />

MENU 4
<img width="160" height="44" alt="Cuplikan layar 2026-04-29 145636" src="https://github.com/user-attachments/assets/7c77a406-d230-4827-af2c-aabe78c906bf" />

OUTPUT JIKA USER TIDAK MENGINPUTKAN ANGKA 
<img width="283" height="68" alt="Cuplikan layar 2026-04-29 150337" src="https://github.com/user-attachments/assets/f1c006fe-28c4-4eed-b0d5-250466bdf7ab" />

LINK : https://youtu.be/4p9XT-ZebyI?si=POpVhRAdTfDzG6FJ
