print("****** Kredit Keaaktifan Mahasiswa ******")
print("(student Activities Credit)")
print("1. Menambahkan Kegiatan")
print("2. Menampilkan Jumlah Poin")
print("3. Keluar")
print("----------------------------")
pilihan = int(input("Silahkan Maasukan pilihan yang Anda: "))
if pilihan == 1:
    def nama_kegiatan():
        kegiatan = str(input("Nama Kegiatan: "))
    nama_kegiatan()
    def tanggal_kegiatan():
        tanggal = str(input("Tanggal Kegiatan: "))
    tanggal_kegiatan()
    def kategori_kegiatan():
        print("Pilihlah Kategori Kegiatan")
        print(" - Prestasi")
        print(" - Organisasi")
        print(" - Kepanitiaan")
        print(" - Rekognisi")
        kategori = str(input("Masukan Kategori Kegiatan: "))
        print("")
        print("Kegiatan berhasil ditambahkan.")
    kategori_kegiatan()
elif pilihan == 2:
    print("")
    print("----------------------------")
    print("Nama Kegiatan    Tanggal     Kategori    Poin")
    
elif pilihan == 3:
    print("Sistem Berhenti...")