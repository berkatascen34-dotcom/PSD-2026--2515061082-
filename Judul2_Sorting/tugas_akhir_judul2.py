def tukar(data, i, j):
    sementara = data[i]
    data[i] = data[j]
    data[j] = sementara


def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                tukar(data, j, j + 1)


def main():
    try:
        jumlah = int(input("Masukkan jumlah siswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    tinggi_siswa = []

    print("Masukkan tinggi badan siswa (cm):")
    for i in range(jumlah):
        while True:
            try:
                tinggi = int(input(f"Tinggi siswa ke-{i+1}: "))
                tinggi_siswa.append(tinggi)
                break
            except ValueError:
                print("Harus berupa angka! Coba lagi.")

    print("\nData tinggi sebelum diurutkan:", tinggi_siswa)

    bubble_sort(tinggi_siswa)

    print("Data tinggi setelah diurutkan (Terpendek → Tertinggi):", end=" ")
    for t in tinggi_siswa:
        print(t, end=" ")
    print()


if __name__ == "__main__":
    main()
