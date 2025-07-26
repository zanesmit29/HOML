from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch()
#     page = browser.new_page()
#     page.goto('https://autbor.com/example3.html')
#     print(page.title())
#     browser.close()

# Running a browser without headless mode
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto('https://autbor.com/example3.html')
browser.close()
playwright.stop()

# Clicking browser buttons
page.go_back()
page.go_forward()
page.reload()
page.reload()

# Finding elements
# page.get_by_role(role, name=label) ## Finding elements by either their role or their label
page.get_by_text(text)
page.get_by_label(label)
page.get_by_placeholder(text)
