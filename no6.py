bukuList = [
    {
        "no_isbn" : "123-456-789",
        "judul" : "Dasar Pemrograman",
        "pengarang" : "Mughis",
        "isiHalaman" : "270",
        "deskripsi" : "Buku Pembelajaran Dasar Pemrograman",
        "stok" : 5,
        "booked" : 2 
    },
    {
        "no_isbn" : "234-567-891",
        "judul" : "Dasar Python",
        "pengarang" : "Bilma",
        "isiHalaman" : "300",
        "deskripsi" : "Panduan lengkap dasar python",
        "stok" : 7,
        "booked" : 2
    },
    {
        "no_isbn" : "345-678-912",
        "judul" : "Kumpulan Dongeng Nusantara",
        "pengarang" : "Feisal",
        "isiHalaman" : "320",
        "deskripsi" : "Sekumpulan cerita dongeng",
        "stok" : 6,
        "booked" : 1
    }
]

def tampilkan_buku():
    print("\nDaftar Buku")
    print("----------------------------------------------------------------------------")
    nomor = 1
    for buku in bukuList:
        print(f"{nomor}.")
        print(f"   ISBN        : {buku['no_isbn']}")
        print(f"   Judul       : {buku['judul']}")
        print(f"   Pengarang   : {buku['pengarang']}")
        print(f"   Isi Halaman : {buku['isiHalaman']}")
        print(f"   Deskripsi   : {buku['deskripsi']}")
        print(f"   Stok        : {buku['stok']}")
        print(f"   Booked      : {buku['booked']}")
        nomor += 1


mahasiswa_list = []

def tambah_mahasiswa_dan_peminjaman():
    print("\nData Mahasiswa yang meminjam ")
    print("----------------------------------------------------------------------------")
    nama =    input("Masukkan nama lengkap      : ")
    nim =     input("Masukkan NIM               : ")
    nomerHp = input("Masukkan Nomor Handphone   : ")
    alamat =  input("Masukkan alamat            : ")

    mahasiswa = {
        "nama"      : nama,
        "NIM"       : nim,
        "nomerHp"   : nomerHp,
        "alamat"    : alamat
    }
    mahasiswa_list.append(mahasiswa)
    print("Mahasiswa berhasil ditambahkan!")
    
    while True:
        tampilkan_buku()
        pilihan_buku = int(input("Pilih nomor buku yang ingin dipinjam: ")) - 1

        if 0 <= pilihan_buku < len(bukuList):
            buku = bukuList[pilihan_buku]
            if int(buku['stok']) > 0:
                tanggalpinjam =   input("Tanggal pinjam (YYYY-MM-DD) : ")
                tanggal_kembali = input("Tanggal kembali (YYYY-MM-DD): ")
                buku['stok'] = str(int(buku['stok']) - 1)
                buku['booked'] = str(int(buku['booked']) + 1)
                peminjam_list.append({
                    "nim"                   : mahasiswa["NIM"],
                    "no_isbn"               : buku['no_isbn'],
                    "tanggalpinjam"         : tanggalpinjam,
                    "tanggal_kembali"       : tanggal_kembali,
                    "status"                : "Dipinjam"
                })
                print("Buku berhasil dipinjam!")
            else:
                print("Buku sudah habis di pinjam.")
        else:
            print("Pilihan buku tidak valid.")
        
        lagi = input("Apakah Anda ingin meminjam buku lain? (y/n): ")
        if lagi.lower() != 'y':
            break

peminjam_list = []

def tampilkan_peminjam():
    print("\nDaftar Peminjam")
    print("----------------------------------------------------------------------------")
    if not peminjam_list:
        print("Belum ada peminjam yang terdaftar.")
    else:
        for peminjam in peminjam_list:
            print(f"NIM                   : {peminjam['nim']}")
            print(f"No ISBN               : {peminjam['no_isbn']}")
            print(f"Tanggal Pinjam        : {peminjam['tanggalpinjam']}")
            print(f"Tanggal Kembali       : {peminjam['tanggal_kembali']}")
            print(f"Status                : {peminjam['status']}\n")

while True:
    print("\nMenu Utama:")
    print("1. Tambah Mahasiswa dan Peminjaman Buku")
    print("2. Tampilkan Daftar Peminjam")
    print("3. Tampilkan Daftar Buku")
    print("4. Keluar")
    
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        tambah_mahasiswa_dan_peminjaman()
    elif pilihan == '2':
        tampilkan_peminjam()
    elif pilihan == '3':
        tampilkan_buku()
    elif pilihan == '4':
        print("----------------------------------------------------------------------------")
        print("Terima kasih telah menggunakan sistem perpustakaan.")
        break
    else:
        print("----------------------------------------------------------------------------")
        print("Pilihan tidak valid. Silakan coba lagi.")