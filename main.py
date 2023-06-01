

modern_sozluk = {"cringe":"Utandırıcı", "lol":"Kahka atmak", "rofl":"yerde gülmekten dönmek", "aggrro":"Sinirlenmek"}

word = input("Anlamadığınız bir kelime yazın: ")


if word.lower() in modern_sozluk.keys():
    print(modern_sozluk[word.lower()])
else:
    print("maalesef kelime sozlukte bulunmadi ")
