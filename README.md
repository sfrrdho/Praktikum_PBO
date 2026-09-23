# Praktikum_PBO
# Sistem Manajemen Data Registrasi Tim dan Klasifikasi Spesifikasi Kendaraan Balap Ketahanan Kelas GT3

## Struktur Class

Sistem memiliki 3 class utama yang saling berinteraksi, yaitu:
1. **`TimBalap`**: Class ini menampung data entitas tim. Atributnya mencakup atribut public (`nama_tim`, `manajer`) dan atribut private (`__anggaran`).
2. **`KendaraanGT3`**: Class yang mengelola spesifikasi mobil. Menyimpan atribut public dan atribut private (`__horsepower`). Memiliki Static Method untuk fungsi bantuan yang tidak memakai data objek.
3. **`RegistrasiBalap`**: Class utama yang menyimpan Atribut Kelas (data yang dipakai bersama oleh seluruh objek) seperti `nama_kejuaraan` dan `total_tim_terdaftar`.

## Penggunaan Materi Modul

*   **Class & Object (Modul 1)**: Pembuatan pola dasar menggunakan `class` dan pembuatan objek dengan mengisikan nilai pada constructor `__init__(self)`.
*   **Atribut & Method (Modul 2)**: 
    *   Menggunakan *Atribut Instance* (unik tiap objek) dan *Atribut Kelas* (dibagi ke semua objek).
    *   Terdapat *Instance Method* (menerima parameter `self`), *Class Method* (menggunakan decorator `@classmethod` dan parameter `cls` untuk *factory method* tipe data *dictionary* serta pengubahan atribut kelas), dan *Static Method* (menggunakan decorator `@staticmethod` tanpa parameter `self`/`cls`).
*   **Encapsulation & Property (Modul 3)**:
    *   Atribut private ditulis dengan dua garis bawah (`__`) agar tidak bisa diakses langsung (*name mangling*).
    *   Menggunakan metode idiomatik Python: Decorator `@property` sebagai *getter* (dipanggil seperti atribut biasa).
    *   Menggunakan decorator `@nama_properti.setter` sebagai *setter* yang menjalankan validasi otomatis (menggunakan blok `if` untuk mencetak peringatan atau memicu `raise ValueError`) sebelum data objek dapat berubah.

## Panduan Pengujian

Untuk menjalankan kode, jalankan file `main.py` menggunakan Python.

Pada blok paling bawah kode, terdapat kode untuk program pengujian:
1. Pembuatan masing-masing 2 objek untuk setiap kelas.
2. Demonstrasi pemanggilan *static method*, *instance method*, dan *class method*.
3. Pengujian *setter*: Terdapat eksperimen memberikan data valid dan data tidak valid pada properti `horsepower` dan `anggaran` untuk membuktikan fungsionalitas proteksi data berjalan semestinya. Baris akhir dibiarkan menjadi komentar agar bisa di-*uncomment* untuk melihat munculnya *ValueError*.
