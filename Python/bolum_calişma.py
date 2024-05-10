# Input ile first_name bilgisini al
# input ile last_name bilgisini al 
# input ile year_of_birth bilgisini al
# first_name ve last_name bilgilerinin karakter sayini yaz
# fString ile kullanicinin adinin ilk harfi ve buyuk olacak sekilde full_name yazdir
# yasini ve gelecek seneki yasini fString ile yazdir
# 18 yasindan buyukse True olacak sekilde bilgisini don

first_name=input("Adınızı yazınız:")
last_name=input("Soyadınızı yazınız:")
year_of_birth=input("Doğum yılınız:")

print(f"Ad Karakter Sayisi: {len(first_name)}, Soyad Karakter Sayisi: {len(last_name)}")


full_name = f"{first_name[0]}. {last_name}".upper()
print(full_name)

print(f"Yasiniz:{2024-int(year_of_birth)},Gelecek Yıl {2024-int(year_of_birth)+1} yasinda olacaksınız")

print(f"Yasiniz 18 den büyük mü : {2024-int(year_of_birth)>18}")