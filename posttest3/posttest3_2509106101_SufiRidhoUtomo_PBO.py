from abc import ABC, abstractmethod
import os

class Pembalap:
    def __init__(self, nama):
        self.nama = nama

    def persiapan_sesi(self):
        return f"Pembalap {self.nama} mengenakan helm dan cek radio."

class Mekanik:
    def __init__(self, nama):
        self.nama = nama

    def persiapan_sesi(self):
        return f"Mekanik {self.nama} sedang memanaskan ban dan cek tekanan ban."

def jalankan_persiapan(aktor):
    print(aktor.persiapan_sesi())


class KendaraanBalap(ABC):
    def __init__(self, merk, model, horsepower):
        self.merk = merk
        self._model = model          
        self.__horsepower = horsepower 

    def __str__(self):
        return f"{self.merk} {self._model} ({self.__horsepower} HP)"

    def __gt__(self, other):
        return self.__horsepower > other.__horsepower

    def cek_status_layak_balap(self):
        return "Kelistrikan, ABS, dan Rem dalam kondisi layak, Bersiap untuk balapan."

    @abstractmethod
    def klasifikasi_mesin(self):
        pass

    @abstractmethod
    def hitung_top_speed(self):
        pass


class MercedesGT3(KendaraanBalap):
    def __init__(self, model, horsepower, aero_package):
        super().__init__("Mercedes-AMG", model, horsepower)
        self.aero_package = aero_package 

    def klasifikasi_mesin(self):
        return "Mesin: 6.2L Naturally Aspirated V8 (Front-Mid Engine)"

    def hitung_top_speed(self):
        return 298 #KM/H 

class PorscheGT3(KendaraanBalap):
    def __init__(self, model, horsepower, aero_package):
        super().__init__("Porsche", model, horsepower)
        self.aero_package = aero_package  

    def klasifikasi_mesin(self):
        return "Mesin: 4.2L Naturally Aspirated Flat-6 (Rear Engine)"

    def hitung_top_speed(self):
        return 295 #KM/H


class Sponsor:
    def __init__(self, nama_perusahaan, nilai_kontrak):
        self.nama_perusahaan = nama_perusahaan
        self.nilai_kontrak = nilai_kontrak

class DokumenRegistrasi:
    def __init__(self, id_registrasi, kategori_kelas):
        self.__id_registrasi = id_registrasi
        self.kategori_kelas = kategori_kelas
    
    def info_dokumen(self):
        return f"ID Reg: {self.__id_registrasi} | Kelas: {self.kategori_kelas}"

class TimBalap:
    def __init__(self, nama_tim, kendaraan):
        self.nama_tim = nama_tim
        self.kendaraan = kendaraan 
        self.dokumen = DokumenRegistrasi(f"REG-{nama_tim[:3].upper()}-2026", "GT3 Pro")
        self.sponsors = []

    def tambah_sponsor(self, sponsor_obj):
        self.sponsors.append(sponsor_obj)

    def tampilkan_profil_tim(self):
        print(f"\n===> Profil Tim: {self.nama_tim} <===")
        print(f"Kendaraan: {self.kendaraan}")
        print(f"Dokumen  : {self.dokumen.info_dokumen()}")
        if self.sponsors:
            list_sponsor = [f"{s.nama_perusahaan} (${s.nilai_kontrak:,})" for s in self.sponsors]
            print(f"Sponsor  : {', '.join(list_sponsor)}")


# <BLOK EKSEKUSI>

if __name__ == "__main__":
    os.system("cls")
    print("===> BUKTI ABSTRAKSI TIDAK BISA DIINSTANSIASI <===")
    try:
        mobil_gagal = KendaraanBalap("Lamborghini", "Huracan", 580)
    except TypeError as e:
        print(f"ERROR TERTANGKAP: {e}\n")

    print("===| IMPLEMENTASI RELASI UML |===")
    mobil_mercedes = MercedesGT3("GT3 Evo", 550, "Standard Diffuser")
    mobil_porsche = PorscheGT3("911 GT3 R (992)", 565, "High Downforce")
    sponsor_redbull = Sponsor("RedBull", 10000000)
    sponsor_kus = Sponsor("KUS", 8000000)
    sponsor_dekra = Sponsor("Dekra", 1500000)
    sponsor_pirelli = Sponsor("Pirelli", 7500000)

    tim_1 = TimBalap("Mercedes-AMG Team Verstappen Racing", mobil_mercedes)
    tim_1.tambah_sponsor(sponsor_redbull)
    tim_1.tambah_sponsor(sponsor_dekra)
    tim_1.tambah_sponsor(sponsor_pirelli)

    tim_2 = TimBalap("Manthey Racing", mobil_porsche)
    tim_2.tambah_sponsor(sponsor_kus)
    tim_2.tambah_sponsor(sponsor_dekra)
    tim_2.tambah_sponsor(sponsor_pirelli)

    tim_1.tampilkan_profil_tim()
    tim_2.tampilkan_profil_tim()

    print("\n===| POLIMORFISME VIA PEWARISAN & OPERATOR OVERLOADING |===")
    koleksi_mobil = [mobil_mercedes, mobil_porsche]
    for mobil in koleksi_mobil:
        print(f"- {mobil}")  
        print(f"  {mobil.klasifikasi_mesin()}")
        print(f"  Top Speed: {mobil.hitung_top_speed()} km/h")
        print(f"  Status   : {mobil.cek_status_layak_balap()}")

    print("\nPerbandingan Tenaga (Operator Overloading __gt__):")
    if mobil_porsche > mobil_mercedes:
        print(f"{mobil_porsche.merk} lebih bertenaga daripada {mobil_mercedes.merk}")
    else:
        print(f"{mobil_mercedes.merk} lebih bertenaga daripada {mobil_porsche.merk}")

    print("\n===| DUCK TYPING (PERSIAPAN TIM) |===")
    driver_merc = Pembalap("Max Verstappen")
    mekanik_merc = Mekanik("Jules Gounon")
    
    driver_por = Pembalap("Kevin Estre")
    mekanik_por = Mekanik("Dennis Olsen")
    
    print("[Mercedes-AMG Team Verstappen Racing]")
    jalankan_persiapan(driver_merc)
    jalankan_persiapan(mekanik_merc)

    print("\n[Manthey Racing]")
    jalankan_persiapan(driver_por)
    jalankan_persiapan(mekanik_por)