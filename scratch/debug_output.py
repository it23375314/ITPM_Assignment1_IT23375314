from playwright.sync_api import sync_playwright
import time

CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
URL = "https://www.pixelssuite.com/chat-translator"

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME_PATH, headless=True)
    page = browser.new_page()
    page.goto(URL)
    page.wait_for_selector('textarea[placeholder*="English"]')
    
    input_ta = page.locator('textarea[placeholder*="English"]')
    output_ta = page.locator('textarea[placeholder*="Sinhala"]')
    btn = page.get_by_role("button", name="Transliterate").first
    
    input_ta.fill("oyata kohomada")
    btn.click()
    print("Clicked Transliterate. Waiting 5s...")
    time.sleep(5)
    
    print(f"Input Value: '{output_ta.input_value()}'")
    print(f"Inner Text: '{output_ta.inner_text()}'")
    print(f"Text Content: '{output_ta.text_content()}'")
    
    # Check if there are other textareas or divs that might have the text
    all_text = page.evaluate("() => document.body.innerText")
    print(f"Is 'ඔයාට' in page? {'ඔයාට' in all_text}")
    
    browser.close()
