def menu():
    print("\n===== SISTEM PENILAIAN =====")
    print("1. Masukkan Nilai")
    print("2. Lihat Nilai")
    print("3. Lihat Rata-rata & Grade")
    print("4. Keluar Program")


def main():
    nilai = [0 for _ in range(5)]
    pelajaran = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "IPA", "IPS"]

    running = True
    while running:
        menu()
        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilihan == 1:
            print("\n=== INPUT NILAI ===")
            for i in range(5):
                while True:
                    try:
                        nilai[i] = int(input(f"Masukkan nilai {pelajaran[i]}: "))
                        break
                    except ValueError:
                        print("Harus angka!")

        elif pilihan == 2:
            print("\n=== DATA NILAI ===")
            for i in range(5):
                print(f"{pelajaran[i]}: {nilai[i]}")

        elif pilihan == 3:
            print("\n=== HASIL NILAI ===")
            total = sum(nilai)
            rata_rata = total / 5

            print(f"Total Nilai: {total}")
            print(f"Rata-rata: {rata_rata}")

            if rata_rata >= 90:
                grade = "A"
            elif rata_rata >= 80:
                grade = "B"
            elif rata_rata >= 70:
                grade = "C"
            elif rata_rata >= 60:
                grade = "D"
            else:
                grade = "E"

            print(f"Grade: {grade}")

        elif pilihan == 4:
            print("Program selesai.")
            running = False

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
