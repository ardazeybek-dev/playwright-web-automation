"""Web Automation Bot (Playwright).

Navigates to the given website, reads the page title, and takes a full-page screenshot.

Settings can be changed via environment variables:
    TARGET_URL   -> address to visit (default: Ege University Bergama Vocational School)
    OUTPUT_PATH  -> file to save the screenshot to (default: bergama_myo.png)
"""

import os
import sys

from playwright.sync_api import sync_playwright

# The Windows console (cp1252) may fail on emoji/Turkish characters; force UTF-8 output.
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

            print(f"🌐 Navigating to: {TARGET_URL}")
            page.goto(TARGET_URL, wait_until="domcontentloaded", timeout=30000)

            page_title = page.title()
            print(f"✅ Successfully reached the site: {page_title}")

            # Short wait for dynamic content on the page to load
            page.wait_for_timeout(3000)

            page.screenshot(path=OUTPUT_PATH, full_page=True)
            print(f"📸 Screenshot saved: {OUTPUT_PATH}")
        finally:
            browser.close()


if __name__ == "__main__":
    try:
        bot_projesi()
    except Exception as e:
        print(f"❌ An error occurred while running the bot: {e}", file=sys.stderr)
        sys.exit(1)
