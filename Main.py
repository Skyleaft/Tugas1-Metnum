# import untuk buat tabel
from tabulate import tabulate

#import method
from Script import bisection_regulafalsi
from Script import newton_secant

#f = soal f(x)= x^3 + 5x^2 - 10x - 4
f = lambda x: x**3 + 5  * x**2 - 10 * x - 4
#masukan kedalam method cari akar dengan parameter (f(x), interval awal, interval akhir, toleransi error, method nya(bisection/regula_falsi))
bisection_regulafalsi.cari_akar(f,1.3,2,0.0001,'bisection')
bisection_regulafalsi.cari_akar(f,1.3,2,0.0001,'regula_falsi')

#fd=turunan f(x)
fd = lambda x: 3 * x**2 + 10 * x - 10
#masukan kedalam method cari akar dengan parameter(f(x), toleransi error, interval awal(tambahkan interval akhir jika method secant), turunan f(x), method nya)
newton_secant.cari_akar(f, 0.0001,[1.3], fd, 'newton')
newton_secant.cari_akar(f, 0.0001,[1.3, 2],method='secant')

print("Tekan enter untuk keluar")
input()
