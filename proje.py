"""Web Otomasyon Botu (Playwright).

Belirtilen web sitesine gider, sayfa başlığını okur ve tam sayfa ekran görüntüsü alır.

Ayarlar ortam değişkenleriyle değiştirilebilir:
    TARGET_URL   -> ziyaret edilecek adres (varsayılan: Ege Ünv. Bergama MYO)
    OUTPUT_PATH  -> ekran görüntüsünün kaydedileceği dosya (varsayılan: bergama_myo.png)
"""

import os
import sys

from playwright.sync_api import sync_playwright

# Windows konsolu (cp1252) emoji/Türkçe karakterlerde hata verebilir; çıktıyı UTF-8'e sabitle.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

TARGET_URL = os.getenv("TARGET_URL", "https://bergamamyo.ege.edu.tr/")
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "bergama_myo.png")


def bot_projesi():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()

            print(f"🌐 Siteye gidiliyor: {TARGET_URL}")
            page.goto(TARGET_URL, wait_until="domcontentloaded", timeout=30000)

            sayfa_basligi = page.title()
            print(f"✅ Başarıyla giriş yapılan site: {sayfa_basligi}")

            # Sayfadaki dinamik içeriğin yüklenmesi için kısa bekleme
            page.wait_for_timeout(3000)

            page.screenshot(path=OUTPUT_PATH, full_page=True)
            print(f"📸 Ekran görüntüsü kaydedildi: {OUTPUT_PATH}")
        finally:
            browser.close()


if __name__ == "__main__":
    try:
        bot_projesi()
    except Exception as e:
        print(f"❌ Bot çalışırken bir hata oluştu: {e}", file=sys.stderr)
        sys.exit(1)
