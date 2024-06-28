from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import os
import tempfile
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the extension relative to the script's directory
path_to_extension = os.path.join(script_dir, "Chrome_Profile", "Extensions", "edibdbjcniadpccecjdfdjjppcpchdlm", "1.1.4_0")

def keep_browser_alive():
    with sync_playwright() as p:
        print("Playwright wurde gestartet...")
        
        # Create a unique temporary directory for user data
        user_data_dir = tempfile.mkdtemp()
        
        try:
            browser = p.chromium.launch_persistent_context(
                user_data_dir,
                channel="chrome",
                headless=False,
                args=[
                    f"--disable-extensions-except={path_to_extension}",
                    f"--load-extension={path_to_extension}",
                    "--autoplay-policy=no-user-gesture-required",
                    "--disable-dev-shm-usage",
                    "--no-sandbox"
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
        
        finally:
            # Clean up the temporary directory
            shutil.rmtree(user_data_dir)

if __name__ == "__main__":
    keep_browser_alive()
