from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the extension relative to the script's directory
path_to_extension = os.path.join(script_dir, "Chrome_Profile", "Extensions", "edibdbjcniadpccecjdfdjjppcpchdlm",
                                 "1.1.4_0")
user_data_dir = os.path.join(script_dir, "Chrome_Profile")


def keep_browser_alive():
    with sync_playwright() as p:
        print("Playwright wurde gestartet...")
        browser = p.chromium.launch_persistent_context(
            user_data_dir,
            channel="chrome",
            headless=False,
            args=[
                f"--disable-extensions-except={path_to_extension}",
                f"--load-extension={path_to_extension}",
                "--autoplay-policy=no-user-gesture-required"
            ],
        )
        page = browser.new_page()
        stealth_sync(page)
        print("Öffne Webseite...")
        page.goto('https://www.browserscan.net/bot-detection')
        print("Seite wurde erfolgreich geöffnet.")

        try:
            while True:
                pass  # Keeps the browser session alive indefinitely
        except KeyboardInterrupt:
            print("Browser session ended by user.")


if __name__ == "__main__":
    keep_browser_alive()
