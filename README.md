# 📸 Instagram Non-Followers Finder

Bu uygulama, Instagram hesabınızda sizi geri takip etmeyen kullanıcıları (unfollowers) tespit etmenizi sağlayan **Tkinter** tabanlı bir masaüstü aracıdır.

---

## ✨ Özellikler

* **Güvenli Giriş:** `instaloader` kütüphanesi kullanılarak resmi olmayan API üzerinden bağlantı sağlar.
* **Gerçek Zamanlı İlerleme:** Veri çekme sırasında `Progressbar` ile işlemin hangi aşamada olduğunu gösterir.
* **Asenkron Çalışma:** `threading` yapısı sayesinde veri çekilirken uygulama arayüzü donmaz.
* **Profil Erişimi:** Listelenen kullanıcı ismine tıklandığında ilgili profili tarayıcıda otomatik açar.
* **Dışa Aktarma:** Sonuçları profil linkleriyle birlikte `.txt` dosyası olarak kaydeder.

---

## 🛠 Kullanılan Teknolojiler

* **Python 3.x**
* **Instaloader:** Instagram profil ve liste yönetimi.
* **Tkinter:** Grafiksel kullanıcı arayüzü (GUI).
* **Webbrowser:** Tarayıcı entegrasyonu.

---

## 🚀 Kurulum ve Çalıştırma

1. Gerekli kütüphaneyi bilgisayarınıza yükleyin:
   ```bash
   pip install instaloader
