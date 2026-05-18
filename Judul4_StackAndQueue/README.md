Tugas Akhir Percobaan 4 


Judul Program : Sistem Antrean Kendaraan 


Program di atas berfungsi untuk mengatur sistem antrean kendaraan menggunakan konsep Queue (antrian) pada struktur data Linked List, di mana kendaraan yang masuk lebih dahulu akan keluar lebih dahulu sesuai prinsip FIFO (First In First Out). Program ini memungkinkan pengguna untuk menambahkan kendaraan ke dalam antrean, mengeluarkan kendaraan dari antrean, melihat kendaraan yang berada di posisi paling depan, serta menampilkan seluruh daftar kendaraan yang sedang mengantre. Selain itu, program juga dapat memantau kondisi kepadatan antrean dengan batas maksimal 10 kendaraan. Jika jumlah kendaraan sudah mencapai atau melebihi batas tersebut, sistem akan memberikan peringatan bahwa antrean padat, sedangkan jika jumlah kendaraan masih di bawah 10 maka sistem akan menampilkan informasi bahwa antrean masih lancar dan aman. Program ini dibuat dengan menu interaktif sehingga mudah digunakan dan dapat membantu pengguna memahami penerapan struktur data queue dalam kehidupan sehari-hari, terutama pada sistem antrean kendaraan.


<img width="1294" height="4738" alt="judul4 ta" src="https://github.com/user-attachments/assets/1ea3e9c8-fc7c-4477-9f35-e1a48689b135" />


Penjelasan Code


**1. `class Node:`**
Bagian ini digunakan untuk membuat sebuah node atau tempat penyimpanan data pada Linked List. Node berfungsi untuk menyimpan data kendaraan dan menghubungkannya dengan data berikutnya dalam antrean.

**2. `def __init__(self, data):`**
Fungsi ini disebut constructor, yaitu fungsi yang otomatis dijalankan saat node baru dibuat. Fungsi ini menerima data kendaraan yang akan dimasukkan ke antrean.

**3. `self.data = data`**
Baris ini berfungsi untuk menyimpan data kendaraan, misalnya nomor kendaraan atau nama kendaraan.

**4. `self.next = None`**
Baris ini digunakan untuk membuat penghubung ke node berikutnya. Nilai awalnya `None` karena node belum terhubung ke data lain.

---

**5. `class QueueKendaraan:`**
Bagian ini digunakan untuk membuat class utama sistem antrean kendaraan.

**6. `self.front_ptr = None`**
Variabel ini berfungsi untuk menyimpan posisi kendaraan paling depan dalam antrean.

**7. `self.rear_ptr = None`**
Variabel ini digunakan untuk menyimpan posisi kendaraan paling belakang dalam antrean.

**8. `self.jumlah = 0`**
Variabel ini berfungsi untuk menghitung jumlah kendaraan yang sedang berada di antrean.

**9. `self.batas = 10`**
Variabel ini digunakan untuk menentukan batas maksimal antrean kendaraan, yaitu 10 mobil.

---

**10. `def is_empty(self):`**
Fungsi ini digunakan untuk mengecek apakah antrean kosong atau tidak.

**11. `return self.front_ptr is None`**
Jika antrean kosong, fungsi akan menghasilkan nilai `True`, sedangkan jika masih ada kendaraan maka menghasilkan `False`.

---

**12. `def enqueue(self, kendaraan):`**
Fungsi ini digunakan untuk menambahkan kendaraan baru ke dalam antrean.

**13. `new_node = Node(kendaraan)`**
Baris ini membuat node baru untuk menyimpan data kendaraan yang dimasukkan pengguna.

**14. `if self.is_empty():`**
Bagian ini mengecek apakah antrean masih kosong.

**15. `self.front_ptr = new_node` dan `self.rear_ptr = new_node`**
Jika antrean kosong, maka kendaraan pertama akan menjadi antrean paling depan sekaligus paling belakang.

**16. `self.rear_ptr.next = new_node`**
Jika antrean sudah memiliki isi, kendaraan baru akan ditambahkan di belakang antrean terakhir.

**17. `self.rear_ptr = new_node`**
Posisi antrean paling belakang diperbarui menjadi kendaraan terbaru.

**18. `self.jumlah += 1`**
Jumlah kendaraan dalam antrean akan bertambah satu.

**19. `print(f"Kendaraan {kendaraan} masuk ke antrean.")`**
Program menampilkan pesan bahwa kendaraan berhasil masuk ke antrean.

**20. `if self.jumlah >= self.batas:`**
Program mengecek apakah jumlah antrean sudah mencapai batas maksimal.

**21. `print("PERINGATAN: Antrean padat!")`**
Jika antrean mencapai 10 kendaraan atau lebih, sistem akan memberi peringatan bahwa antrean padat.

**22. `print("Antrean lancar dan aman.")`**
Jika antrean masih di bawah batas maksimal, sistem memberi informasi bahwa kondisi antrean masih aman.

---

**23. `def dequeue(self):`**
Fungsi ini digunakan untuk mengeluarkan kendaraan dari antrean.

**24. `if self.is_empty():`**
Program mengecek apakah antrean kosong.

**25. `print("Antrean kosong.")`**
Jika kosong, program akan menampilkan pesan bahwa tidak ada kendaraan di antrean.

**26. `temp = self.front_ptr`**
Data kendaraan paling depan disimpan sementara.

**27. `print(f"Kendaraan {temp.data} keluar dari antrean.")`**
Program menampilkan kendaraan yang keluar dari antrean.

**28. `self.front_ptr = self.front_ptr.next`**
Posisi antrean depan dipindahkan ke kendaraan berikutnya.

**29. `if self.front_ptr is None:`**
Jika antrean sudah habis, maka antrean belakang juga dikosongkan.

**30. `self.rear_ptr = None`**
Menandakan bahwa antrean benar-benar kosong.

**31. `self.jumlah -= 1`**
Jumlah kendaraan dikurangi satu karena ada kendaraan yang keluar.

---

**32. `def peek(self):`**
Fungsi ini digunakan untuk melihat kendaraan paling depan tanpa mengeluarkannya dari antrean.

**33. `print(f"Kendaraan paling depan: {self.front_ptr.data}")`**
Program menampilkan kendaraan yang berada di posisi paling depan.

---

**34. `def display(self):`**
Fungsi ini digunakan untuk menampilkan seluruh daftar kendaraan dalam antrean.

**35. `current = self.front_ptr`**
Variabel `current` digunakan untuk membaca antrean mulai dari depan.

**36. `while current is not None:`**
Perulangan dilakukan selama masih ada kendaraan dalam antrean.

**37. `print("-", current.data)`**
Program menampilkan satu per satu kendaraan dalam antrean.

**38. `current = current.next`**
Berpindah ke kendaraan berikutnya.

**39. `print(f"Jumlah kendaraan dalam antrean: {self.jumlah}")`**
Menampilkan total kendaraan yang sedang mengantre.

**40. `print("Status: Antrean padat!")`**
Menampilkan status padat jika antrean mencapai batas maksimal.

**41. `print("Status: Antrean lancar dan aman.")`**
Menampilkan status aman jika antrean masih normal.

---

**42. `def main():`**
Fungsi utama program yang digunakan untuk menjalankan seluruh sistem antrean.

**43. `antrean = QueueKendaraan()`**
Membuat objek antrean kendaraan.

**44. `while pilih != 5:`**
Program akan terus berjalan sampai pengguna memilih menu keluar.

**45. `print("=== SISTEM ANTREAN KENDARAAN ===")`**
Menampilkan judul menu program.

**46. `pilih = int(input("Pilih menu: "))`**
Pengguna diminta memilih menu yang tersedia.

**47. `except ValueError:`**
Digunakan untuk menangani kesalahan jika pengguna memasukkan input selain angka.

**48. `if pilih == 1:`**
Menu untuk menambahkan kendaraan ke antrean.

**49. `elif pilih == 2:`**
Menu untuk mengeluarkan kendaraan dari antrean.

**50. `elif pilih == 3:`**
Menu untuk melihat kendaraan paling depan.

**51. `elif pilih == 4:`**
Menu untuk menampilkan seluruh antrean kendaraan.

**52. `elif pilih == 5:`**
Menu untuk keluar dari program.

---

**53. `if __name__ == "__main__":`**
Bagian ini memastikan program utama dijalankan saat file Python dibuka.

**54. `main()`**
Menjalankan fungsi utama program antrean kendaraan.







