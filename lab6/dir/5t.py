filename = "text2.txt"
text = ("Пах-пах-пах қандай ғажап иіс. ", "Шат-шат-шат қиялыма ілес")
with open (filename, "w", encoding="utf-8") as file:
    for item in text:
      txt = file.write(item)