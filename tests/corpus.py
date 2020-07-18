import elotl.corpus

print("Name\t\tDescription")
list_of_corpus = elotl.corpus.list_of_corpus()
for row in list_of_corpus:
    print(row)

print()
axolotl = elotl.corpus.load('axolotlr')
if axolotl == 0:
    print("El nombre ingresado no corresponde a ningun corpus")

print()
axolotl = elotl.corpus.load('axolotl')
if axolotl == 0:
    print("El nombre ingresado no corresponde a ningun corpus")
else:
    for row in axolotl[:5]:
        print(row)

print()
tsunkua = elotl.corpus.load('tsunkua')
if tsunkua == 0:
    print("El nombre ingresado no corresponde a ningun corpus")
else:
      for row in tsunkua[:5]:
          print(row[0]) # lengua_no_originaria
          print(row[1]) # lengua_originaria
          print(row[2]) # variante
          print(row[3]) #nombre_de_documento
