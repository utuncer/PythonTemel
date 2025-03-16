
#print("hello world")
# isim = "Muhammed" #string
# fiyat = 13.52 #float
# x = 3 #integer
# AldiMi = True # boolean



# kitapIsmi = "Moby Dick"
# kitapSayfasi = 195
# kitapAgirligi = 13.45
# kitapYeniMi = True
# print(type(kitapAgirligi)) #Değşkenin türünü öğrenmek için (<class 'float'>)


#Kullanıcıdan değer alma işlemleri

# isim = input("İsminiz Nedir? ")
# print("Hoşgeldin " + isim)

# isim = input("Merhabalar adınız nedir? ")
# yemek = input("En sevdiğiniz yemek nedir? ")

# print(isim + " " + yemek + " sever")


#Tür Değiştirme

# int()
# float()
# str()
# bool()


#Matematik İşlemleri
# x=9
# y=5
# print(x//y)#Bu işlem sayıları tam olarak böler . dan sonrak değeriyazpmaz örneğin 9/5 1.8 ken ekrana 1 yazar
# print(x**y)#Bu işlem x üzeri y olarak üslü sayı işlemi yapmaya yarar

# sayi1 = input("1. Sayıyı girinz: ")
# sayi2 = input("2. Sayıyı girinz: ")
# print(int(sayi1) + int(sayi2))


#Matematik Fonksiyonlar
# print(round(9.5)) # yuvarlama işlemidir virgülden sonraki 5 ve 5'den büyük değerleri bir üst sayıya altındakileri bir alt sayıya yuvarlar çıktı = 10
# print(abs(-9)) # Mutlak değer alma işlemidir
#SAYİNİN karekökünü almak için dışarıdan kütüphane eklenmeli
# import math
# print(math.sqrt(9))
# min(9,2,5) # En küçük değer
# max(9,2,5) # En büyük değer

#String

# isim = "Muhammed" 
# print(isim[0:3]) #0->M 3->a 0'dan 3'e doğru gider ama son girilen değeri almak çıktı = Muh
# print(isim[-1]) #son harfi yazar

#String Fonksiyonları

# print(len(isim)) # Metnin uzunluğunu öğrenmek için
# print(isim.title()) #Örneğin birden fazla kelimeli bir cümle varsa her kelimenin başındaki harfi büyük yazar
# print(isim.upper()) #Tüm harfleri büyütür
# print(isim.lower()) #Tüm harfleri küçültür
# print(isim.find("M")) #Metodun çalıştırdığı değerde e harfi değerin kaçıncı harfii onu yazdırır. Böyle bir değer olmaddığında -1 değerini verir
# print(isim.replace("e","s")) # Metodun ilk parametresine değiştirmek istediğin değeri ikinci parametresine istediğin yeni değeri giriyorsun
# isim = input("İsminizi giriniz: ")
# print(isim.title())

#Mantıksal Operatörler

# arabanVarMi = True
# ehliyetinVarMi = False

# if arabanVarMi and ehliyetinVarMi:
#     print("Trafiğe çıkabilirsin")
# elif arabanVarMi and not ehliyetinVarMi:
#     print("Araban var ve henüz ehliyetin yoksa trafiğe çıkamazsın")
# elif arabanVarMi or ehliyetinVarMi:
#     print("Trafiğe çıkmana az kaldı")
# else:
#     print("Trafiğe çıkmana uzun bir yol var")