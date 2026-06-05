# Playwright Final Projesi

Bu proje, Python ve Playwright kütüphanesi kullanılarak geliştirilmiş bir web otomasyon botudur.

## Proje Hakkında
- Ege Üniversitesi Bergama Meslek Yüksekokulu web sitesine otomatik giriş yapar.
- Sayfa başlığını okuyup terminale yazdırır.
- Sayfanın tam ekran görüntüsünü alır.

## Docker ile Çalıştırma
Proje tamamen Dockerize edilmiştir. Çalıştırmak için:
1. Bilgisayarınızda Docker'ın açık olduğundan emin olun.
2. Terminalde proje klasöründeyken şu komutu çalıştırın:
   `docker-compose up --build`
3. Bot arka planda (headless) çalışacak ve `bergama_myo.png` dosyasını otomatik olarak ana klasöre çıkaracaktır.