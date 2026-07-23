# Playwright Web Otomasyon Botu

Python ve Playwright kütüphanesi kullanılarak geliştirilmiş bir web otomasyon botu.

## Proje Hakkında
- Ege Üniversitesi Bergama Meslek Yüksekokulu web sitesine otomatik olarak gider.
- Sayfa başlığını okuyup terminale yazdırır.
- Sayfanın tam ekran görüntüsünü alıp `bergama_myo.png` olarak kaydeder.

## Docker ile Çalıştırma
Proje tamamen Dockerize edilmiştir:
1. Bilgisayarınızda Docker'ın çalıştığından emin olun.
2. Proje klasöründe:
   ```bash
   docker-compose up --build
   ```
3. Bot arka planda (headless) çalışır ve `bergama_myo.png` dosyasını ana klasöre çıkarır.

## Docker Olmadan Yerel Çalıştırma
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# macOS / Linux:
# source venv/bin/activate

pip install -r requirements.txt
playwright install chromium

python proje.py
```

## Ayarlar (opsiyonel)
Ortam değişkenleriyle hedef site ve çıktı dosyası değiştirilebilir:

| Değişken      | Varsayılan                        | Açıklama                          |
|---------------|-----------------------------------|----------------------------------|
| `TARGET_URL`  | `https://bergamamyo.ege.edu.tr/`  | Ziyaret edilecek adres           |
| `OUTPUT_PATH` | `bergama_myo.png`                 | Ekran görüntüsünün kayıt yolu    |

Örnek:
```bash
TARGET_URL="https://ege.edu.tr" OUTPUT_PATH="ege.png" python proje.py
```
