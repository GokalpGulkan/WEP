first_name="gokalp"
last_name="gulkan"
full_name= first_name +" "+last_name

#str nin ilk karakteri
print(first_name[0] , last_name[0])

# belli bir yerden başlayan bilgi [3:10]
print(first_name[2:200],last_name[3:6])

#baştan 3 karakter
print(first_name[:3])

# son 3 karakter
print(first_name[-3:])

#ters çevir [::-1]
print(first_name[::-1])


#tümü büyük harf yapma upper
print(first_name.upper())
print(first_name.upper(),last_name.upper())


#ilk harfi büyük capitalize
print(first_name.capitalize())

#ilk harfleri büyük title
print(first_name.title(),last_name.title())

#ters çevir swapcase
print(first_name.swapcase())


#kuçuk harf olsun
print(first_name.lower())

#say count
print(first_name.count("g"),last_name.count("g"))


#liste içindekileri birleştir join

names = ["mehmet","cem","ahmet","ali"]
print(" ".join(names))

#parçala /ayır  split
print(full_name.split(" "))


#SOR::

#baslik seklinde mi ?  istitle
print(last_name.istitle())

#hepsi kucuk harf mi ? islower

print(full_name.islower())

#belli bir karakterle başlıyor mu  startswicth
print(full_name.startswith("h"))

#belli bir karakterle bitiyor mu endswith
print(full_name.endswith("n"))

#aradığım bilgi str içinde var mi ? find
print(full_name.find("3"))

#belli bir bilgiyi değiştir replace
print(full_name.lower().replace("gokalp gulkan","GÖKALP GÜLKAN"))

#Birden fazla değişken içindeki bilgiyi birleştirmek
full_name=f"merhaba {first_name} {last_name}"

print(full_name)

#hesaplama yaparak str sonucu donmek
print("sonuc:",10*10)

#function içinde yapılan hesaplamanın sonucunu dönmek
def calculate(number):
    return number*number
result = f"sonuc {calculate(10)}"
print("fonks kullanıldı:",result)

#uzun iceriklerin belli bir kısmını göstermek
print(f"{result[:4]}")

#yazıları ortalamak veya sağa yaslamak
print("-"*30)
print(f"{'Django':->30}")
print(f"{'Python':-^30}")
#belli bir uzunluktaki int yapılar oluşturmak :00034 gibi
number=34
print(f"{number:06d}")
