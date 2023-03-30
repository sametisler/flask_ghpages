import random
def tc_kimlik_no_uret():
    """
    Bu fonksiyon " https://tr.wikipedia.org/wiki/T.C._Kimlik_Numaras%C4%B1 " adresindeki kurallara göre tc kimlik numarası üretir.
    """
    tc_kimlik_no = ""
    tc_numbers = random.choices(range(1,10), k = 1) #1 ve 9 arasında rastgele bir rakamı tc_numbers listesine ilk eleman olarak atar.
    tc_numbers += random.choices(range(0,10), k = 8) #0 ve 9 arasında rastgele sekiz rakamı tc_numbers listesine eleman olarak atar.
    # Yazılı kurallara göre 10. ve 11. elemanı atar.
    tc_numbers.append((sum([tc_numbers[i] for i in range(0, 9, 2)])*7 + sum([tc_numbers[i] for i in range(1, 9, 2)])*9)%10) 
    tc_numbers.append((sum([tc_numbers[i] for i in range(0, 9, 2)])*8)%10)
    # if bloğu ilk 10 rakamın toplamının ilk basamağını 11. elemana eşit olduğunu kontrol eder.
    if sum([tc_numbers[i] for i in range(0, 10)]) % 10 == tc_numbers[-1]:
        for i in tc_numbers:
            tc_kimlik_no += str(i) # değişkene liste elemanlarını string olarak yazdırır.
        return tc_kimlik_no
    else:
        print("Hata")
print(tc_kimlik_no_uret())