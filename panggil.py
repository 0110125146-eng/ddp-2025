import Bangunruang as br
import bangundatar as bd

print("~~~ BANGUN RUANG ~~~")
print(f"Volum Kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"Volum balok adalah {br.balok(4, 5, 2)}")
print(f"Volum Prisma Segitiga adalah {br.prisma(5,4,5)}")
print(f"Volum Tabung adalah {br.tabung(5,10)}")
print(f"Volum Kerucut adalah {br.Kerucut(5, 12)}")

print("~~~ BANGUN DATAR ~~~")
print(f"Luas Persegi adalah {bd.luas_persegi(5)}")
print(f"Luas Persegi Panjang adalah {bd.luas_persegi_panjang(20,10)}")
print(f"Luas Segitiga adalah {bd.luas_segitiga(10,5)}")
print(f"Luas Lingkaran adalah{bd.luas_lingkaran(8)} ")
print(f"Luas JajarGanjar adalah {bd.jajarGanjar(4,7)}")