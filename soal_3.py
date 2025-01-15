from modul_soal_3 import Stack

antrian1 = Stack()
antrian1.push("Joko")
antrian1.push("Aji")
antrian1.push("Haris")

while True:
    for i, data in enumerate(antrian1.items,1):
        print(f'Antrian Ke-{i} {data}')
    antrian1.tampilan()
    pilih = int(input('Masukan Pilihan : '))
    print("="*100)
    if pilih == 1:
        nama = str(input("Masukan Nama :"))
        antrian1.push(nama.capitalize())
        1
        print("="*100)
    if pilih == 2:
        antrian1.pop()
    if pilih == 3:
        keluar = str("Ingin Keluar Program? (Y/T) : ").upper()
        if keluar == "Y":
            break