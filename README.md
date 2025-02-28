## Nama     : Zizantara Arzeva Cakra Kahana

## NIM      : 312410398

## Kelas    : TI,24.A.3

# Logika_Informatika-2

## 1. Fungsi Utama: `hitung_biaya_pengiriman()`

```python
def hitung_biaya_pengiriman(berat_paket, jarak_pengiriman, jenis_pengiriman, status_keanggotaan):
```

Fungsi ini menerima 4 parameter:
- `berat_paket`: Nilai numerik yang mewakili berat paket dalam kilogram
- `jarak_pengiriman`: Nilai numerik yang mewakili jarak pengiriman dalam kilometer
- `jenis_pengiriman`: String yang menunjukkan jenis pengiriman ('biasa' atau 'express')
- `status_keanggotaan`: String yang menunjukkan apakah pelanggan member atau non-member

### Proses Perhitungan:

1. **Inisialisasi biaya dasar**: 
   ```python
   biaya_total = 10000
   ```
   Setiap pengiriman dimulai dengan biaya dasar Rp 10.000

2. **Pengecekan berat paket**:
   ```python
   if berat_paket > 5:
       biaya_total += 5000
   ```
   Jika berat paket lebih dari 5kg, tambahkan Rp 5.000 ke biaya total

3. **Pengecekan jarak pengiriman**:
   ```python
   if jarak_pengiriman > 10:
       biaya_total += 8000
   ```
   Jika jarak pengiriman lebih dari 10km, tambahkan Rp 8.000 ke biaya total

4. **Pengecekan jenis pengiriman**:
   ```python
   if jenis_pengiriman.lower() == 'express':
       biaya_total += 20000
   ```
   Jika jenisnya express, tambahkan Rp 20.000 ke biaya total
   
   Catatan: `.lower()` digunakan agar case-insensitive (tidak peduli huruf besar/kecil)

5. **Penanganan diskon member**:
   ```python
   biaya_sebelum_diskon = biaya_total
   
   if status_keanggotaan.lower() == 'member':
       diskon = biaya_sebelum_diskon * 0.1
       biaya_total -= diskon
   ```
   - Menyimpan total biaya sebelum diskon
   - Jika status member, memberikan diskon 10% dari total biaya sebelum diskon
   - Mengurangi diskon dari total biaya

6. **Return nilai akhir**:
   ```python
   return biaya_total
   ```
   Fungsi mengembalikan total biaya setelah semua perhitungan

## 2. Fungsi `main()`

Fungsi ini bertugas menangani interaksi dengan pengguna dan menjalankan program:

1. **Tampilan awal**:
   ```python
   print("=== PROGRAM PENGHITUNG BIAYA PENGIRIMAN ===")
   print("Ketentuan biaya pengiriman:")
   # ... informasi ketentuan ...
   ```
   Menampilkan informasi tentang program dan aturan biaya

2. **Blok `try-except`**:
   ```python
   try:
       # kode input dan perhitungan
   except ValueError:
       print("\nError: Masukkan angka yang valid untuk berat paket dan jarak pengiriman.")
   ```
   Menangkap error jika pengguna memasukkan input yang tidak valid (bukan angka)

3. **Input data dari pengguna**:
   ```python
   berat_paket = float(input("Masukkan berat paket (kg): "))
   jarak_pengiriman = float(input("Masukkan jarak pengiriman (km): "))
   ```
   Meminta pengguna memasukkan berat dan jarak, dan mengkonversi input ke tipe data float

4. **Input jenis pengiriman**:
   ```python
   print("\nPilih jenis pengiriman:")
   print("1. Biasa")
   print("2. Express")
   jenis_pilihan = input("Masukkan pilihan (1/2): ")
   
   if jenis_pilihan == '1':
       jenis_pengiriman = 'biasa'
   elif jenis_pilihan == '2':
       jenis_pengiriman = 'express'
   else:
       print("Pilihan tidak valid. Menggunakan jenis pengiriman biasa.")
       jenis_pengiriman = 'biasa'
   ```
   - Menampilkan pilihan jenis pengiriman
   - Meminta input dari pengguna
   - Mengkonversi input menjadi string 'biasa' atau 'express'
   - Menggunakan nilai default 'biasa' jika input tidak valid

5. **Input status keanggotaan**:
   ```python
   print("\nStatus keanggotaan:")
   print("1. Member")
   print("2. Non-member")
   status_pilihan = input("Masukkan pilihan (1/2): ")
   
   if status_pilihan == '1':
       status_keanggotaan = 'member'
   elif status_pilihan == '2':
       status_keanggotaan = 'non-member'
   else:
       print("Pilihan tidak valid. Menggunakan status non-member.")
       status_keanggotaan = 'non-member'
   ```
   Mirip dengan jenis pengiriman, meminta input status keanggotaan dan mengkonversi ke string yang sesuai

6. **Memanggil fungsi perhitungan**:
   ```python
   biaya_total = hitung_biaya_pengiriman(berat_paket, jarak_pengiriman, jenis_pengiriman, status_keanggotaan)
   ```
   Memanggil fungsi utama dengan parameter yang telah diinput

7. **Menampilkan hasil**:
   ```python
   print("\n=== RINCIAN BIAYA PENGIRIMAN ===")
   print(f"Berat paket: {berat_paket} kg")
   # ... informasi lainnya ...
   print(f"TOTAL BIAYA: Rp {biaya_total:,.2f}".replace(",", "."))
   ```
   - Menampilkan semua detail input
   - Menampilkan total biaya dengan format yang sesuai 
   - `.replace(",", ".")` mengubah pemisah ribuan dari koma menjadi titik (format Indonesia)

## 3. Blok `if __name__ == "__main__":`

```python
if __name__ == "__main__":
    main()
```

Baris ini memastikan fungsi `main()` dieksekusi ketika program dijalankan langsung (bukan diimpor sebagai modul).

## Contoh Perhitungan:

1. **Skenario 1**: 
   - Berat: 3 kg (≤ 5 kg, tidak ada biaya tambahan)
   - Jarak: 8 km (≤ 10 km, tidak ada biaya tambahan)
   - Jenis: Biasa (tidak ada biaya tambahan)
   - Status: Non-member (tidak ada diskon)
   - Total: Rp 10.000 (hanya biaya dasar)

2. **Skenario 2**:
   - Berat: 6 kg (> 5 kg, +Rp 5.000)
   - Jarak: 15 km (> 10 km, +Rp 8.000)
   - Jenis: Express (+Rp 20.000)
   - Status: Member (diskon 10%)
   - Perhitungan: 
     - Biaya dasar: Rp 10.000
     - Tambahan berat: Rp 5.000
     - Tambahan jarak: Rp 8.000
     - Tambahan express: Rp 20.000
     - Subtotal: Rp 43.000
     - Diskon (10%): Rp 4.300
     - Total akhir: Rp 38.700

Program ini dirancang dengan prinsip modularitas dan penanganan error yang baik, sehingga mudah dipahami dan digunakan.