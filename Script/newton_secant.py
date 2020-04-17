# import untuk buat tabel
from tabulate import tabulate

def cari_akar(f,e,x=[],fd=None ,method=''):
    colomHeader=["Iterasi","Xn","f(xn)","f'(xn)","|xn - xn+1|","| Era |"]
    iterasi = [1]
    list_f = []
    list_fd = []
    list_xxn = []
    list_gra = []

    if(method == 'newton'):
        if fd is None:
            print("Masukan arg fd(Function Derivative)!")
        else:
            print("Metode \t\t\t: Newton Raphson")
            list_fd = [round(fd(x[0]), 6)]
            list_xxn += [None]
            list_gra += [None]
            g = lambda b: round(b - (f(b) / fd(b)), 6)
    elif(method == 'secant'):
        if len(x) != 2:
            print("Masukan list arg x dengan 2 nilai")
        else:
            print("Metode \t\t\t: Secant")
            list_xxn += [round(abs(x[-1] - x[-2]), 6)]
            list_f += [round(f(x[0]), 6)]
            colomHeader[2] = "f(xn-1)"
            colomHeader[3] = "f(xn)"
            colomHeader.insert(1, "xn-1")
            iterasi[0] = 1
            g = lambda x0, x1: round(x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0)), 6)
    else:
        print("pilih metode 'newton' atau 'secant' ke dalam arg method!")
        return

    while True:
        list_f += [round(f(x[-1]), 6)]

        if method == 'newton':
            x += [g(x[-1])]
            list_fd += [round(fd(x[-1]), 6)]
        elif method == 'secant':
            x += [g(x[-1])]
            list_fd += [round(fd(x[-1]), 6)]

        list_xxn += [round(abs(x[-1] - x[-2]), 6)]
        list_gra += [round(abs((x[-1] - x[-2]) / x[-1]), 6)]

        if list_xxn[-1] < e:
            print("Berhenti karena : Lebar selang baru")
            break
        elif list_gra[-1] < e:
            print("Berhenti Karena : Galat Relatif hampiran akar")
            break
        else:
            iterasi += [iterasi[-1] + 1]

    if (method == 'newton'):
        iterasi += [iterasi[-1] + 1]
        table = zip(iterasi, x, list_f, list_fd, list_xxn, list_gra)
    elif (method == 'secant'):
        xn = x[:]
        x.pop(0)
        table = zip(iterasi, xn, x, list_f, list_fd, list_xxn, list_gra)

    print("Akar didapatkan : {}".format(str(x[-1])))
    print()
    print(tabulate(table, headers=colomHeader))