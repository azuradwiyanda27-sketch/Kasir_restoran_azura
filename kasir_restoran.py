# ===== 1. MULAI PROGRAM =====
print("=" * 40)
print("   APLIKASI KASIR RESTORAN")
print("=" * 40)

total = 0  # variabel untuk menyimpan total belanja

# ===== 2. TAMPILKAN MENU MAKANAN =====
menu = {
    1: ("Nasi Goreng", 25000),
    2: ("Mie Ayam", 15000),
    3: ("Ayam Geprek", 20000),
    4: ("Sate Ayam", 30000),
    5: ("Bakso", 18000),
}

# ===== 3 & 4. PROSES PEMESANAN (perulangan sampai pilih 0) =====
while True:
    print("\n--- DAFTAR MENU ---")
    for kode, (nama, harga) in menu.items():
        print(f"{kode}. {nama:<12} - Rp{harga:,}".replace(",", "."))
    print("0. Selesai Memilih")

    pilihan = int(input("\nPilih menu (0-5): "))

    # Apakah pilihan 0? Ya -> keluar dari perulangan
    if pilihan == 0:
        break

    # Validasi: pilihan harus 1-5
    if pilihan not in menu:
        print("Pilihan tidak valid, coba lagi.")
        continue

    jumlah = int(input("Masukkan jumlah pesanan: "))
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0.")
        continue

    nama, harga = menu[pilihan]
    subtotal = harga * jumlah
    total += subtotal  # subtotal ditambahkan ke total
    print(f"-> {nama} x{jumlah} = Rp{subtotal:,}".replace(",", "."))

# ===== 5. HITUNG DISKON =====
if total > 200000:
    persen_diskon = 20
else:
    persen_diskon = 0

potongan = total * persen_diskon // 100
total_bayar = total - potongan

# ===== 6. TAMPILKAN STRUK PEMBAYARAN =====
def rupiah(angka):
    return "Rp" + f"{angka:,}".replace(",", ".")

print("\n" + "=" * 40)
print("        STRUK PEMBAYARAN")
print("=" * 40)
print(f"Total Belanja : {rupiah(total)}")
print(f"Diskon        : {persen_diskon}%")
print(f"Potongan      : {rupiah(potongan)}")
print("-" * 40)
print(f"Total Bayar   : {rupiah(total_bayar)}")
print("=" * 40)
print("          Terima Kasih")