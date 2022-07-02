
metin = (input("Cümleyi Giriniz\n"))
metin = metin.lower()
a_kelime = (input("Aramak İstediğiniz Kelimeyi Giriniz\n"))
a_kelime= a_kelime.lower()
result = metin.count(a_kelime)
print("Metinde Aradığnız Harf ",result," Tane Bulunmuştur.\n")
