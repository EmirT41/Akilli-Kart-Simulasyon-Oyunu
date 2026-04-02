🃏 Akıllı Sporcu Kart Ligi Simülasyonu
Bu proje, Kocaeli Sağlık ve Teknoloji Üniversitesi (KOSTÜ) Mühendislik ve Doğa Bilimleri Fakültesi bünyesinde, Bilgisayar/Yazılım Mühendisliği bölümü için geliştirilmiş nesneye yönelik bir kart oyunu simülasyonudur.

🎯 Projenin Amacı
Projenin temel hedefi, bilgisayar ile kullanıcı arasında oynanan, Nesneye Yönelik Programlama (OOP) prensiplerine uygun, dinamik puanlama sistemine sahip bir strateji oyunu geliştirmektir.

🚀 Öne Çıkan Özellikler
Geniş Kart Havuzu: sporcular.txt dosyasından okunan 24 farklı sporcu kartı.
Branş Bazlı Oynanış: Futbol, Basketbol ve Voleybol branşlarının sırasıyla oynandığı tur sistemi.
Dinamik Puanlama: Kartların performansı; temel özellikler, enerji seviyesi, moral bonusları ve seviye çarpanları ile anlık olarak hesaplanır.
Yapay Zeka Stratejileri: * Kolay: Rastgele kart seçimi yapar.Orta: Enerjisi en yüksek olan kartı seçerek stratejik hamle yapar.
İstatistik ve Kayıt: Kullanıcı girişleri ve maç skorları .csv dosyalarında kalıcı olarak saklanır.

🛠 Kullanılan Teknolojiler
Programlama Dili: Python
Arayüz Tasarımı: PyQt6 kütüphanesi.
Veri Depolama: CSV ve TXT formatında dosya tabanlı veri yönetimi.
Tasarım Araçları: Diyagramlar için draw.io ve Gemini yardımı

🏗 Nesneye Yönelik Programlama (OOP) Uygulamaları
Kalıtım (Inheritance): Sporcu ana sınıfından türetilen branş sınıfları.
Soyutlama (Abstraction): Sporcu ve KartSecmeStratejisi sınıflarının ABC (Abstract Base Class) olarak tanımlanması.
Kapsülleme (Encapsulation): Kart özelliklerinin ve performans hesaplama mantığının sınıflar içinde gizlenmesi.
Çok Biçimlilik (Polymorphism): Her branşın performansHesapla metodunu kendi kurallarına göre çalıştırması.

📦 Kurulum ve Çalıştırma
Uygulamanın çalışabilmesi için sisteminizde Python yüklü olmalıdır.
pip install PyQt6 ile PyQt kütüphanesini kurunuz.
Ve sonra python main.py ile uygulamayı başlatın.

👥 Proje Ekibi
Mustafa Emirhan Turhan - Bilal Furkan Ceylan

📊 Yazılım Mimarisi
Model Katmanı: Sporcu ve Strateji nesne tanımları.
Mantık Katmanı: Oyun kuralları ve puanlama yönetimi.
Servis Katmanı: Dosya depolama ve kullanıcı işlemleri.
Arayüz Katmanı: PyQt6 tabanlı kullanıcı etkileşimi.

Bu proje 31.03.2026 tarihinde tamamlanmış olup ileride daha gelişmiş halini yapmayı planlıyoruz.

