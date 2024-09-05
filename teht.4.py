kaupungit = []

for i in range(5):
    kaupunki = input(f"Anna kaupungin nimi ({i+1}/5): ")
    kaupungit.append(kaupunki)

print("Syöttämäsi kaupungit ovat:")
for kaupunki in kaupungit:
    print(kaupunki)
