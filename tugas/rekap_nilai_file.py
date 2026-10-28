
def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                # Lewati baris kosong
                if not baris:
                    continue

                try:
                    # Memisahkan NIM dan nilai
                    nim, teks_nilai = baris.split(",")
                    nim = nim.strip()
                    teks_nilai = teks_nilai.strip()

                    if not nim:
                        raise ValueError("NIM kosong")

                    nilai = float(teks_nilai)

                    # Simpan data yang valid
                    data.append((nim, nilai))

                except ValueError:
                    print(f"Baris {nomor} dilewati: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data


def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    nilai = [item[1] for item in data]

    jumlah_data = len(nilai)
    rata_rata = sum(nilai) / jumlah_data
    nilai_minimum = min(nilai)
    nilai_maksimum = max(nilai)
    jumlah_lulus = sum(1 for x in nilai if x >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Minimum: {nilai_minimum:.2f}\n")
        file.write(f"Maksimum: {nilai_maksimum:.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")

        file.write("\nDaftar nilai valid:\n")
        for nim, angka in data:
            status = "Lulus" if angka >= 60 else "Tidak lulus"
            file.write(f"{nim},{angka:.2f},{status}\n")


def main():
    input_file = "data/nilai.txt"
    output_file = "data/hasil_rekap.txt"

    data = baca_data(input_file)

    if data:
        tulis_rekap(output_file, data)
        print(f"Rekap berhasil ditulis ke {output_file}")
    else:
        print("Rekap tidak dibuat karena tidak ada data valid.")


if __name__ == "__main__":
    main()
