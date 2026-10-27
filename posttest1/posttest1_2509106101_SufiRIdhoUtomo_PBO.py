class TimBalap:
    def __init__(self, nama_tim, manager, anggaran):
        self.nama_tim = nama_tim
        self.manager = manager
        self.__anggaran = anggaran

    def tampilkan_info(self):
        print(f"Tim: {self.nama_tim} | Manager: {self.manager} | Anggaran: {self.__anggaran}")

    @property
    def anggaran(self):
        return self.__anggaran

    @anggaran.setter
    def anggaran(self, nilai_baru):
        if nilai_baru < 0:
            raise ValueError("Anggaran Tidak Boleh Negatif.")
        self.__anggaran = nilai_baru

class KendaraanGT3:
    def __init__(self, manufaktur, model, berat_kg, horsepower):
        self.manufaktur = manufaktur
        self.model = model
        self.berat_kg = berat_kg
        self.__horsepower = horsepower

    def tampilkan_spesifikasi(self):
        print(f"Kendaraan: {self.manufaktur} {self.model} | Berat: {self.berat_kg}kg | Power: {self.__horsepower} HP")

    @property
    def horsepower(self):
        return self.__horsepower

    @horsepower.setter
    def horsepower(self, nilai_baru):
        if nilai_baru < 500:
            print("Horsepower Tidak Boleh Kurang Dari 500 HP.")
        else:
            self.__horsepower = nilai_baru

    @staticmethod
    def validasi_berat_minimum(berat_kg):
        if berat_kg >= 1200:
            return True
        return False

class RegistrasiBalap:
    nama_kejuaraan = "Nurburgring 24 Hours"
    musim = "2026"
    total_tim_terdaftar = 0

    def __init__(self, tim, kendaraan, nomor_start):
        self.tim = tim
        self.kendaraan = kendaraan
        self.nomor_start = nomor_start
        RegistrasiBalap.total_tim_terdaftar += 1

    def cetak_bukti_registrasi(self):
        print(f"[{RegistrasiBalap.nama_kejuaraan} {RegistrasiBalap.musim}] - Entri #{self.nomor_start}")
        print(f"Terdaftar: Tim {self.tim.nama_tim} dengan Manager {self.tim.manager} menggunakan {self.kendaraan.manufaktur}")

    @classmethod
    def ubah_musim(cls, musim_baru):
        cls.musim = musim_baru

    @classmethod
    def dari_dict(cls, data):
        return cls(data["tim"], data["kendaraan"], data["nomor_start"])

#===========| Uji Running |===========#

tim1 = TimBalap("Mercedes-AMG Team Verstappen Racing", "Raymond Vermeulen", 25000000000)
tim2 = TimBalap("Manthey Racing", "Nicolas Raeder", 23000000000)

tim1.tampilkan_info()
tim2.tampilkan_info()

mobil1 = KendaraanGT3("Mercedes-AMG", "GT3 EVO", 1250, 590)
mobil2 = KendaraanGT3("Porsche", "911 GT3 R", 1210, 565)

print(f"Apakah Mercedes-AMG GT3 EVO Memenuhi Syarat Minimum Berat? {KendaraanGT3.validasi_berat_minimum(mobil1.berat_kg)}")
print(f"Apakah Porsche 911 GT3 R Memenuhi Syarat Minimum Berat? {KendaraanGT3.validasi_berat_minimum(mobil2.berat_kg)}")

mobil1.tampilkan_spesifikasi()
mobil2.tampilkan_spesifikasi()

reg1 = RegistrasiBalap(tim1, mobil1, 3)

data_reg2 = {"tim": tim2, "kendaraan": mobil2, "nomor_start": 911}
reg2 = RegistrasiBalap.dari_dict(data_reg2)

reg1.cetak_bukti_registrasi()
reg2.cetak_bukti_registrasi()

mobil1.horsepower = 510
mobil1.tampilkan_spesifikasi()

mobil2.horsepower = 450
mobil2.tampilkan_spesifikasi()