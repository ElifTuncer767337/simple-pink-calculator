import tkinter as tk
class Calculator:
    
    def __init__(self, baslangic_sayisi=0):
        self.hafiza = baslangic_sayisi 
       
    def toplama(self, sayi):
        self.hafiza = self.hafiza + sayi
        print("Güncel Sonuç: ", self.hafiza)

    def cikarma(self, sayi):
        self.hafiza = self.hafiza - sayi
        print("Güncel Sonuç: ", self.hafiza)

    def carpma(self, sayi):
        self.hafiza = self.hafiza * sayi
        print("Güncel Sonuç: ", self.hafiza)

    def bolme(self, sayi):
        if sayi == 0:
            print('Hata: Bir sayı sıfıra bölünemez!')
        else:
            self.hafiza = self.hafiza / sayi
            print("Güncel Sonuç: ", self.hafiza)

def buton_tikla(sayi):
        mevcut = ekran.get()
        ekran.delete(0, tk.END)
        ekran.insert(0, mevcut + str(sayi))

def islem_sec(sembol):
        global ilk_sayi, secilen_islem
        ilk_sayi = float(ekran.get()) #ekranda yazan sayıyı alıp ondalıklı sayıya çeviriyoruz.
        secilen_islem =sembol #hangi işlemleri seçtiğimizi aklımızda tutuyoruz.
        ekran.delete(0, tk.END)  # ikinci sayı yazılabilsin diye ekranı temizliyoruz.
def sil():
     mevcut =ekran.get()
     if mevcut:
          ekran.delete(len(mevcut) - 1, tk.END)
def hesapla():
    ikinci_sayi = float(ekran.get())
    hesap_makinem.hafiza = ilk_sayi
    
    if secilen_islem == "+":
        hesap_makinem.toplama(ikinci_sayi)
    elif secilen_islem == "-":
        hesap_makinem.cikarma(ikinci_sayi)
    elif secilen_islem == "*":
        hesap_makinem.carpma(ikinci_sayi)
    elif secilen_islem == "/":
        hesap_makinem.bolme(ikinci_sayi)
        
    ekran.delete(0, tk.END)
    ekran.insert(0, str(hesap_makinem.hafiza))
# Pencere kurulumu

pencere = tk.Tk()
pencere.configure(bg='#FFF0F5')
pencere.title("Calculator")

# Ekran (Giriş Kutusu)
ekran = tk.Entry(pencere, width=20, font=("Arial", 16), bg="white", fg="#4A4A4A", justify= "right", bd= 0, insertwidth=2)
ekran.grid(row=0, column=0, columnspan=4)

# --- SATIR 1 ---
buton7 = tk.Button(pencere, text="7", width=7, height=3,font=("Arial", 12, "bold"), bg="#FFB6C1", fg="white",command=lambda: buton_tikla(7))
buton7.grid(row=1, column=0)

buton8 = tk.Button(pencere, text="8", width=7, height=3,font=("Arial", 12, "bold"), bg="#FFB6C1", fg="white", command=lambda: buton_tikla(8))
buton8.grid(row=1, column=1)

buton9 = tk.Button(pencere, text="9", width=7, height=3,font=("Arial", 12, "bold"), bg="#FFB6C1", fg="white", command= lambda: buton_tikla(9))
buton9.grid(row=1, column=2)

buton_arti = tk.Button(pencere, text="+", width=7, height=3,font=("Arial", 12, "bold"), bg="#E0E0E0", fg="#4A4A4A", command =lambda: islem_sec("+"))
buton_arti.grid(row=1, column=3)

# --- SATIR 2 ---
buton4 = tk.Button(pencere, text="4", width=7, height=3,font=("Arial", 12, "bold"), bg="#FFB6C1", fg="white", command= lambda: buton_tikla(4))
buton4.grid(row=2, column=0)

buton5 = tk.Button(pencere, text="5", width=7, height=3, font=("Arial", 12, "bold"), bg="#FFB6C1", fg="white",command= lambda: buton_tikla(5))
buton5.grid(row=2, column=1)

buton6 = tk.Button(pencere, text="6", width=7, height=3,font=("Arial", 12, "bold"), bg="#FFB6C1", fg="white",command= lambda: buton_tikla(6))
buton6.grid(row=2, column=2)

buton_eksi = tk.Button(pencere, text="-", width=7, height=3,font=("Arial", 12, "bold"), bg="#E0E0E0", fg="#4A4A4A", command =lambda: islem_sec("-"))
buton_eksi.grid(row=2, column=3)

# --- SATIR 3 ---
buton1 = tk.Button(pencere, text="1", width=7, height=3,font=("Arial", 12, "bold"), bg="#FFB6C1", fg="white",command= lambda: buton_tikla(1))
buton1.grid(row=3, column=0)

buton2 = tk.Button(pencere, text="2", width=7, height=3,font=("Arial", 12, "bold"), bg="#FFB6C1", fg="white",command= lambda: buton_tikla(2))
buton2.grid(row=3, column=1)

buton3 = tk.Button(pencere, text="3", width=7, height=3,font=("Arial", 12, "bold"), bg="#FFB6C1", fg="white",command= lambda: buton_tikla(3))
buton3.grid(row=3, column=2)

buton_carpma = tk.Button(pencere, text="*", width=7, height=3,font=("Arial", 12, "bold"), bg="#E0E0E0", fg="#4A4A4A", command =lambda: islem_sec("*"))
buton_carpma.grid(row=3, column=3)

# --- SATIR 4 ---
buton0 = tk.Button(pencere, text="0", width=7, height=3,font=("Arial", 12, "bold"), bg="#FFB6C1", fg="white",command= lambda: buton_tikla(0))
buton0.grid(row=4, column=0)

buton_del = tk.Button(pencere, text ="DEL", width = 7, height =3,font=("Arial", 12, "bold"), bg="#E0E0E0", fg="#4A4A4A", command = sil)
buton_del.grid(row=4, column=1)

buton_bolme = tk.Button(pencere, text="/", width=7, height=3,font=("Arial", 12, "bold"), bg="#E0E0E0", fg="#4A4A4A", command =lambda: islem_sec("/"))
buton_bolme.grid(row=4, column=2)

buton_esittir = tk.Button(pencere, text="=", width=7, height=3,font=("Arial", 12, "bold"), bg="#FF1493", fg="white",command =hesapla )
buton_esittir.grid(row=4, column=3)


hesap_makinem = Calculator(0)

# Pencerenin sürekli açık kalmasını sağlayan ana döngü (En sonda olmalı)
pencere.mainloop()