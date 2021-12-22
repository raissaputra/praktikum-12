class Nilai:
    nim = ""
    nama = ""
    jurusan = ""
    __tugas = 0  # PRIVATE ATTRIBUTE
    __uts = 0  # PRIVATE ATTRIBUTE
    __uas = 0  # PRIVATE ATTRIBUTE

    def __init__(self, vnim, vnama, vjurusan):
        self.nim = vnim
        self.nama = vnama
        self.jurusan = vjurusan

    def set_Tugas(self, nilai):
        self.__tugas = nilai

    def get_Tugas(self):
        return self.__tugas

    def set_uts(self, nilai):
        self.__uts = nilai

    def get_uts(self):
        return self.__uts

    def set_uas(self, nilai):
        self.__uas = nilai

    def get_uas(self):
        return self.__uas

    def cetak(self):
        return (0.3 * self.get_Tugas())+(0.35 * self.get_uts())+(0.35 * self.get_uas())

    def tampilkan(self):
        print("Nim: {}\nNama: {}\nJurusan: {}".format(
            self.nim, self.nama, self.jurusan))

    def hapus(self):
        pass

    def ubah(self):
        pass


# INSTANCE CLASS
mhs1 = Nilai("12345", "Alfin Cou", "Teknik Informatika")
print("| --Tampilkan Data-- |")
mhs1.tampilkan()

# UBAH NILAI ATRIBUT
mhs1.set_Tugas(100)
mhs1.set_uts(50)
mhs1.set_uas(90)

print("\n| --Cetak Data Nilai yang sudah di ubah-- |")
mhs1.tampilkan()
print(("Nilai tugas :"), mhs1.get_Tugas())
print(("Nilai uts :"), mhs1.get_uts())
print(("Nilai uas :"), mhs1.get_uas())

# TAMPILKAN NILAI AKHIR
print("\n| --Tampilkan Perhitungan Nilai Akhir-- |")
print(("Nilai Akhir :"), mhs1.cetak())
