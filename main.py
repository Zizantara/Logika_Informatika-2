def hitung_biaya_pengiriman(berat_paket, jarak_pengiriman, jenis_pengiriman, status_keanggotaan):
    biaya_total = 10000
    
    if berat_paket > 5:
        biaya_total += 5000
    if jarak_pengiriman > 10:
        biaya_total += 8000
    if jenis_pengiriman.lower() == 'express':
        biaya_total += 20000
        biaya_sebelum_diskon = biaya_total
    if status_keanggotaan.lower() == 'member':
        diskon = biaya_sebelum_diskon * 0.1
        biaya_total -= diskon
    return biaya_total

def main():
    print("=== PROGRAM PENGHITUNG BIAYA PENGIRIMAN ===")
    print("Ketentuan biaya pengiriman:")
    print("- Biaya dasar: Rp 10.000")
    print("- Tambahan Rp 5.000 jika berat paket > 5 kg")
    print("- Tambahan Rp 8.000 jika jarak pengiriman > 10 km")
    print("- Tambahan Rp 20.000 jika menggunakan layanan express")
    print("- Diskon 10% untuk member")
    print("=" * 45)
    
    try:
        berat_paket = float(input("Masukkan berat paket (kg): "))
        jarak_pengiriman = float(input("Masukkan jarak pengiriman (km): "))
        
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

        biaya_total = hitung_biaya_pengiriman(berat_paket, jarak_pengiriman, jenis_pengiriman, status_keanggotaan)

        print("\n=== RINCIAN BIAYA PENGIRIMAN ===")
        print(f"Berat paket: {berat_paket} kg")
        print(f"Jarak pengiriman: {jarak_pengiriman} km")
        print(f"Jenis pengiriman: {jenis_pengiriman}")
        print(f"Status keanggotaan: {status_keanggotaan}")
        print("-" * 30)
        print(f"TOTAL BIAYA: Rp {biaya_total:,.2f}".replace(",", "."))
        
    except ValueError:
        print("\nError: Masukkan angka yang valid untuk berat paket dan jarak pengiriman.")

if __name__ == "__main__":
    main()