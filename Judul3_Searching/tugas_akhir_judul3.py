def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = [75, 85, 90, 75, 60, 95, 85, 70, 75, 80, 90, 65, 85, 75, 95]
    n = len(data)
    print(f"Daftar Nilai Siswa: {data}")
    while True:
        try:
            target = int(input("Masukkan nilai yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")
    counter = sequential_search(data, n, target)
    if counter > 0:
        print(f"Nilai {target} ditemukan sebanyak {counter} siswa.")
    else:
        print(f"Nilai {target} tidak ditemukan.")


if __name__ == "__main__":
    main()
