class kalkulator:
    def tambah(self,a,b):
        hasil = a+b
        print(f"hasil dari {a}{o}{b} adalah {hasil}")
    def kurang(self,a,b):
        hasil = a-b
        print(f"hasil dari {a}{o}{b} adalah {hasil}")
    def kali(self,a,b):
        hasil = a*b
        print(f"hasil dari {a}{o}{b} adalah {hasil}")
    def bagi(self,a,b):
        if b == 0:
            print("tidak bisa dibagi 0")
        else:
            hasil = a/b
            print = (f"hasil dari {a}{o}{b} adalah {hasil}")
                
cal = kalkulator()
while True:
    print("aplikasih kalkulator sederhana")
    print("==============================")
    print("1. kakulator")
    print("2. keluar")
    s1 = int(input("masukan pilihan 1/2: "))
    if s1 ==1:
        a = int(input("masukan angka pertama: "))
        b = int(input("masukan angka kedua: "))
        print("=metode operasi=")
        print("penjumlahan")
        print("pengurangan")
        print("perkalian")
        print("pembagian")
        o = str(input("masukan operasi: "))
        if o =='+':
            cal.tambah(a,b)
        elif o =='-':
            cal.kurang(a,b)
        elif o =='*':
            cal.kali(a,b)
        elif o =='/':
            cal.bagi(a,b)      
        elif s1 == 2:
                print("terima kasih")
        