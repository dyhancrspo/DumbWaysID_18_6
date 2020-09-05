print('========Vending Machine DumbWaysID========')
totalBeli = int(input("Masukkan Total Pembelian : "))
uangBayar = int(input("Masukkan Jumlah Uang Pembayaran : "))
uangPecahan = [50000, 20000, 10000, 5000, 2000, 1000, 500]
results = [0]*len(uangPecahan)
jumlahUangKembalian = uangBayar - totalBeli
sisaKembali = jumlahUangKembalian
for index, i in enumerate(uangPecahan):
    results[index], sisaKembali = divmod(sisaKembali, i)
print('==========================================')
print("Jumlah Uang Kembali : Rp.%d" % jumlahUangKembalian)
for x, i in zip(results, uangPecahan):
    print("    %d lembar %d" % (x, i))
