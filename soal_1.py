data_mahsiswa = [
    {'NIM': "24090093", 'NAMA': "Fajar Abdul Aziz"},
]

while True:

    nim = int(input("Masukan NIM : "))
    nama = str(input("Masukan Nama : "))
    template = {"NIM": nim, "NAMA": nama}
    data_mahsiswa.append(template)
    print("="*100)
    tampil = str(input("Ingin Tambah Lagi? (Y/T) : ")).upper()
    if tampil == "T":
        print(data_mahsiswa)
        break
