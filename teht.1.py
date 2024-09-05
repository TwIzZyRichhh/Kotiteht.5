import random

n=int(input("Anna arpakuutioiden määrä: "))

summma=0

for i in range(n):
    heitto=random.randint(1,6)
    summma+=heitto

print(f"Arpakuutioiden silmälukujen summa 0n {summma}")