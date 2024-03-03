input1 = input("Bir kelime giriniz: ")
input1 = input1.replace(" ", "")
girdi1_sirala = sorted(input1.lower())

input2 = input("Bir kelime giriniz: ")
input2 = input2.replace(" ", "")
girdi2_sirala = sorted(input2.lower())

kosul1 = bool(girdi1_sirala == girdi2_sirala)

print(kosul1)
