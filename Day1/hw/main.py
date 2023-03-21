# int (integer): Tam sayıları ifade etmek için kullanılan veri tipidir. Örneğin, 5, -3, 0 

# float: Ondalıklı sayıları ifade etmek için kullanılan veri tipidir. Örneğin, 3.14, -0.5 

# str (string): Metinleri ifade etmek için kullanılan veri tipidir. Örneğin, Hello, World!, "Python programlama dili"

# bool (boolean): Sadece iki değer alabilen bir veri tipidir: True (doğru) ve False (yanlış).

# list: Birden fazla değeri aynı anda tutmak için kullanılan veri tipidir. Değerler virgülle ayrılarak 
#       köşeli parantez içinde gösterilir. Örneğin, [1, 2, 3], ["elma", "armut", "portakal"] gibi.

# tuple: Listelerle benzer bir yapıda olup, ancak değiştirilemez (immutable) bir veri tipidir. Parantez içinde gösterilir. 
#        Örneğin, (1, 2, 3), ("elma", "armut", "portakal") gibi.

# set: Birçok benzersiz (unique) elemanın aynı anda saklanmasını sağlayan bir veri tipidir. 
#      Elemanlar süslü parantez içinde gösterilir. Örneğin, {1, 2, 3}, {"elma", "armut", "portakal"} gibi.

# dict (dictionary): Anahtar-değer (key-value) çiftlerinin saklanmasını sağlayan bir veri tipidir. 
#                    Anahtarlar ve değerler iki nokta üst üste işaretiyle ayrılır ve çift tırnak içinde gösterilir.
#                    Örneğin, {"isim": "Ahmet", "yaş": 25} gibi.

# ******************************************

# userName = "kodlama.io" (string)

# age = 32 (int)

# score = 8.5 (float) 

# ******************************************

userName = input("Kullanıcı adını giriniz: ")
password = input("Parolanızı giriniz: ")

test_name = "cem"
test_pass = "123"

if userName == test_name and test_pass == password:
    print("Hoşgeldiniz, ", userName)
else:
    print("Hata")
