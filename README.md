PROJE ADI :  A SİMPLE CALCULATOR 

PROJENİN AMACI VE VİZYONU 

Bu projede, temel matematiksel fonksiyonları yerine getiren ve modern UI/UX 
prensiplerine uygun masaüstü tabanlı bir hesap makinesi geliştirdim. Amaç, nesne yönelimli 
programlama (OOP) ile dinamik kullanıcı arayüzlerinin entegrasyonunu sağlamaktır. 
Hesap makinem dört temel işlemi yapabilmek üzerine tasarlandı. (+,-, /, *)

PROJEDE KULLANILAN TEKNOLOJİLER 

• Python: Projenin ana programlama dili. 
• Tkinter: Grafik kullanıcı arayüzü (GUI) için kullanılan Python'ın standart 
kütüphanesi. 
• OOP (Object-Oriented Programming): Kodun sürdürülebilir ve modüler olması 
için kullanılan yaklaşım. 

SİSTEM MİMARİSİ VE KOD YAPISI 

Arka plan mantığı: class calculator: Bu sınıfın  uygulamın bir hafızası olduğunu , 
arka planda aritmetik işlemlerin döndüğünü ve verilerin terminale anlık basıldığını belirtir. 
Kullanıcı Arayüzü :Butonlar, ekran (Entry) ve bu butonların tetiklediği arayüz 
fonksiyonları (buton_tikla, sil, hesapla). 

UI / UX TASARIM SÜRECİ VE FONKSİYONELLİK 

Görsel Geliştirmeler: Kullanıcı deneyimini artırmak için buton boyutlarını büyüttüm, 
(width, height), sayıların okunaklı olması için sağa yasladım (justify="right"). 

Renk paleti seçimlerim şu şekildedir:  
Pencere Arka Planı: #FFF0F5 (Lavanta Pembesi) tonda seçilerek ferah bir taban 
oluşturdum. 
Sayı Butonları (0-9): #FFB6C1 (Açık Pembe) rengiyle kullanıcıyı yormayacak yumuşak bir 
tona kavuşturdum 
İşlem Butonları (+, -, , /, DEL): #E0E0E0 (Yumuşak Gri) ve koyu füme yazı rengiyle 
(#4A4A4A) tasarlayarak sayı butonlarından net bir şekilde ayırt edilmesini sağladım. 
Eşittir Butonu (=): İşlemi sonlandıran en kritik buton olduğu için odağı artırmak adına 
#FF1493 (Canlı Derin Pembe) rengiyle vurguladım. 

Hata Yönetimi ve Kritik Fonksiyonlar: Kullanıcının hatalı veri girişini engellemek için 
DEL (silme) fonksiyonunu ekledim.
