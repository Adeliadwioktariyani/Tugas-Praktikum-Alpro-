# Program Kalkulator Bunga Tabungan

import interest
import display

print("=== Program Kalkulator Bunga Tabungan ===")

# Input data tabungan
principal = float(input("Masukkan saldo awal (contoh: 80000): "))
rate = float(input("Masukkan bunga tahunan (misal 5% -> 0.05): "))
years = int(input("Masukkan lama menabung (tahun): "))

# Menghitung bunga majemuk
ci = interest.compound_interest(principal, rate, years)

# Menghitung bunga sederhana
si = interest.simple_interest(principal, rate, years)

# Menampilkan hasil perhitungan
display.print_result(principal, rate, years, ci, si)
