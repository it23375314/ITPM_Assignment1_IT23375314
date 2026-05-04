from playwright.sync_api import sync_playwright

CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
URL = "https://www.pixelssuite.com/chat-translator"

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME_PATH, headless=True)
    page = browser.new_page()
    page.goto(URL)
    page.wait_for_load_state("networkidle")
    
    textareas = page.locator("textarea").all()
    print(f"Found {len(textareas)} textareas:")
    for i, ta in enumerate(textareas):
        placeholder = ta.get_attribute("placeholder")
        print(f"[{i}] Placeholder: '{placeholder}'")
        
    buttons = page.locator("button").all()
    print(f"\nFound {len(buttons)} buttons:")
    for i, btn in enumerate(buttons):
        text = btn.inner_text()
        print(f"[{i}] Text: '{text}'")
        
    browser.close()
