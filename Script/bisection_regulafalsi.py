# import untuk buat tabel
from tabulate import tabulate

def cari_akar(f,a,b,e,method):
    if(f(a)*f(b)>=0):
        print("Tidak ada akar pada interval [{}, {}]!".format(str(a),str(b)))
        return
    colomHeader=["Iterasi","a","b","c","f(a)","f(c)","|a - b|","| Era |","f(a).f(c)"]

    if(method == 'bisection'):
        print("Metode       :   Bagi dua (Bisection)")
        g = lambda x, y: round((x + y) / 2, 6)
    elif(method == 'regula_falsi'):
        print("Metode   :   Regula Falsi (False Positive)")
        g = lambda x, y: round(y - (f(y) * (y - x)) / (f(y) - f(x)), 6)
        colomHeader.insert(5, "f(b)")
    else:
        print("pilih metode 'bisection' atau 'regula_falsi' ke dalam arg method!")
        return

    c_t=0
    iterasi = [1]
    list_a = [a]
    list_b = [b]
    list_c = []
    list_fa = []
    list_fb = []
    list_fc = []
    list_fafc = []
    list_ab = []
    list_gra = []

    while True :
        c=g(a,b)
        list_c+=[c]

        list_fa += [round(f(a),6)]
        list_fb += [round(f(b), 6)]
        list_fc += [round(f(c), 6)]
        list_ab += [round(abs(a-b), 6)]
        list_gra += [round(abs((c - c_t) / c), 6)]

        if(list_fc[-1]==0):
            print("Berhenti karena : f(c) = 0")
            break
        elif list_ab[-1] <e:
            print("Berhenti karena : Lebar selang baru")
            break
        elif abs(list_fc[-1]) <e:
            print("Berhenti karena : f(c) < e")
            break
        elif list_gra[-1] < e:
            print("Berhenti karena : Galat relatif hampiran akar")
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_t=c
        list_a += [a]
        list_b += [b]
        iterasi += [iterasi[-1] + 1]

    list_gra[0] = None
    list_fafc = [a * b for a,b in zip(list_fa,list_fc)]

    if(method == 'bisection'):
        table = zip(iterasi,list_a,list_b,list_c,list_fa,list_fc,list_ab,list_gra,list_fafc)
    elif(method == 'regula_falsi'):
        table = zip(iterasi,list_a,list_b,list_c,list_fa,list_fb,list_fc,list_ab,list_gra,list_fafc)

    print("Akar didapatkan : {}".format(str(list_c[-1])))
    print()
    print(tabulate(table,headers=colomHeader))