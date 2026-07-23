# CLAUDE.md

Bu dosya, bu depoda çalışırken Claude Code'a (claude.ai/code) rehberlik eder.

## Proje

Python + Playwright ile yazılmış bir web otomasyon botu. `proje.py`, hedef siteye gidip başlığı
okur ve tam sayfa ekran görüntüsü alır. Tek dosyalık, bağımlılığı az bir script.

## Çalıştırma

- Docker: `docker-compose up --build`
- Yerel: `pip install -r requirements.txt && playwright install chromium && python proje.py`

## Kurallar

- Bot **headless** çalışır; başlığı stdout'a yazar, çıktıyı `OUTPUT_PATH`'e kaydeder.
- Hedef URL ve çıktı yolu ortam değişkenlerinden (`TARGET_URL`, `OUTPUT_PATH`) okunur; sabit değer gömme.
- Bu proje bir script'tir, web servisi değildir — statik hosting'e (ShipStatic vb.) deploy edilmez.
