# import untuk buat tabel
from tabulate import tabulate

#import method
from Script import bisection_regulafalsi
from Script import newton_secant


f = lambda x: x**3 + 5  * x**2 - 10 * x - 4
#bisection_regulafalsi.cari_akar(f,1.3,2,0.0001,'bisection')

#bisection_regulafalsi.cari_akar(f,1.3,2,0.0001,'regula_falsi')

fd = lambda x: 3 * x**2 + 10 * x - 10
newton_secant.cari_akar(f, 0.0001,[1.3], fd, 'newton')