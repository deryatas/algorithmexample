dizi = []
n= int (input())
for i  in range (n):
    sayi = int (input('Sayıyı Gir: '))
    dizi.append(sayi)
    dizi.sort(reverse = False)
    print("eleman sayisi:", len(dizi))
    if n==1:
       print("tek elemanlıd dizi")
    else:
     print("Liste İçindeki En Büyük Sayı :", max(dizi), "\nListe İçindeki En Küçük Sayı :", min(dizi))

    fark= max(dizi)-min(dizi)
    print("fark",fark)
    
    def medyanBul(dizi):
     dizi = sorted(dizi)
     n = len(dizi)
     if n % 2 == 1:
        return dizi[n // 2] 
     else:
        i = n // 2
        return (dizi[i - 1] + dizi[i]) / 2
    medyan=medyanBul(dizi)
    print("medyan", medyan)
    

            

    
     