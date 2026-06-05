from playwright.sync_api import sync_playwright

def bot_projesi():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://bergamamyo.ege.edu.tr/", wait_until="domcontentloaded")
        
        sayfa_basligi = page.title()
        print(f"Başarıyla giriş yapılan site: {sayfa_basligi}")
        
        page.wait_for_timeout(3000)

        page.screenshot(path="bergama_myo.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    bot_projesi()