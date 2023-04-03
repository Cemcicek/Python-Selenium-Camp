from human import Human
import matematik as math

math.bol(20,2)


# sınıflar => classlar
# modules
# paket yönetimi
# self => this


# instance => örnek
human1 = Human("Enes")
human1.talk("Merhaba")
human1.walk()
print(human1)


human2 = Human("Halit")
human2.talk("Selam")
human2.walk()
print(human2)

Human("Melike").talk("Merhaba")