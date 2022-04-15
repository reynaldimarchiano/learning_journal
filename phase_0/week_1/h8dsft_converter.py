# def kelvincelcius(x):
#     x=float(x)
#     x -= 273.15
#     print(x)
#     return x

# def kelvinfahrenheit(x):
#     x=float(x)
#     x=fahrenheitcelcius(kelvincelcius(x))
#     print(x)
#     return x

# def celciuskelvin(x):
#     x=float(x)
#     x += 273.15
#     print(x)
#     return x

# def celciusfahrenheit(x):
#     x=float(x)
#     x = (9/5 * x) + 32 
#     print(x)
#     return x
    
# def fahrenheitcelcius(x):
#     x=float(x)
#     x=(x-32)*5/9
#     print(x)
#     return x

# def fahrenheitkelvin(x):
#     x=fahrenheitcelcius(x)+273.15
#     print(x)
#     return x

# kelvincelcius(373.15)
# kelvinfahrenheit(373.15)
# celciuskelvin(100)
# celciusfahrenheit(100)
# fahrenheitcelcius(212)
# fahrenheitkelvin(212)



# print("tes")

def kelvincelcius(nilai,satuan):
    if satuan.upper() =='K':
        nilai=float(nilai)
        nilai -= 273.15
        print(nilai,'C')
    else:
        print('salah satuan suhu')
    return nilai

def kelvinfahrenheit(nilai,satuan):
    if satuan.upper() =='K':
        nilai=float(nilai)
        nilai=fahrenheitcelcius(kelvincelcius(nilai,satuan),satuan)
        print(nilai,'F')
    return nilai

def celciuskelvin(nilai,satuan):
    if satuan.upper() == 'C':
        nilai=float(nilai)
        nilai += 273.15
        print(nilai,'K')
    else:
        print('salah satuan suhu')
    return nilai

def celciusfahrenheit(nilai, satuan):
    if satuan.upper() == 'C':
        nilai=float(nilai)
        nilai = (9/5 * nilai) + 32
        print(nilai, 'F')
    else:
        print('salah satuan suhu')
    return nilai

def fahrenheitcelcius(nilai, satuan):
    if satuan.upper() == 'F':
        nilai=float(nilai)
        nilai=(nilai-32)*5/9
        print(nilai,satuan='C')
    else:
        print('salah satuan suhu')
    return nilai

def fahrenheitkelvin(nilai,satuan):
    if satuan.upper() == 'F':
        nilai=fahrenheitcelcius(nilai,satuan)+273.15
        print(nilai, 'K')
    else:
        print('salah satuan suhu')
    return nilai



nilai = input("Masukkan nilai suhu : ")
satuan = input("Masukkan satuan dari nilai suhu (C / F / K): ")

if satuan.upper() == 'K':
    pilihan = input("Konversi ke Celcius atau Fahrenheit? (C / F) : ")
    if pilihan.upper() == 'C':
        kelvincelcius(nilai,satuan)
    elif pilihan.upper() == 'F':
        kelvinfahrenheit(nilai,satuan)
    # else:
    #     print('salah satuan suhu')