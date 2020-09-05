const nilaiInput = [1, 2, 3, 4, 5];
for (let i = 0; i < nilaiInput.length; i++) {
	// Membuat Array untuk digunakan di tiap iterasi
	let newNilaiInput = [1, 2, 3, 4, 5];
	// Menghapus nilai pada Array ke-i
	let angka = newNilaiInput.splice(i, 1);
	// Menjumlahkan isi Array
	let jumlah = newNilaiInput.reduce((x, y) => x + y);
	console.log(
		"Angka ke",
		angka,
		":",
		newNilaiInput,
		"dijumlahkan menjadi =",
		jumlah,
	);
}
