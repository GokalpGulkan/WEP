#test skoru 45 alti ise kaldi
#test skoru 75 ve üzeri sie iyi
#test skoru 85 ve üzeri ise pekiyi
#test skoru rakamsal bilgi içermeli
#test skoru 45 ve üzeri ise geçer
#test skoru 0 ila 100 arasında olmalı
#test skoru 55 ve üzeri ise orta



test_score=input("Test Skorunu Giriniz:")
result=""

if not test_score.isdigit():
    print("Lutfen rakamsal bilgi giriniz.")
elif 0<= int(test_score)<=100:
    test_score=int(test_score)
    if test_score >= 85:
        result="pekiyi"
    elif test_score >=75:
        result="iyi"
    elif test_score >=55:
        result="orta"
    elif test_score >=45:
        result="geçer"
    else:
        result="kaldı"
else:
    print("0-100 arası rakam giriniz.")


print(result)


