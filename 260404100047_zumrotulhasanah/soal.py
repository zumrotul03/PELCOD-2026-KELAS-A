  # Program Berbelanja di supermarket
# input
nama = input("masukkan nama pembeli:")
harga = float(input("masukkan harga barang:"))
jumlah = int(input("masukkan jumlah barang:"))

#hitung total harga 
total_harga = harga * jumlah

#percabangan diskon 
if total_harga >= 100000:
    diskon_persen  = 10
    diskon = total_harga * 10 / 100
else:
    diskon_persen = 0
    diskon = 0

# hitung total bayar 
total_bayar = total_harga - diskon 

# output 
print("\n==== HASIL BELANJA ====")
print("nama pembeli : ", ana)
print("total harga : RP ", 24)



