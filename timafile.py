#***open***  
a = open("testtimafile","r")
print(a.read())
a.close()
####open nujno peredova file i rejim raboty.
s = open("forever_young", "w")
s.write("i love you\n")
s.write("sgdhfgj")
s.close()

ingus =open("forever_young", "r")
print(ingus.readlines())
ingus.close()

dagas = open("fyoung","x")
dagas.close()

