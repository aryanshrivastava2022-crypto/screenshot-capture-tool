import pyautogui
from datetime import datetime

print("📸 Screenshot Capture Tool")

input("Press Enter to capture screenshot...")

screenshot = pyautogui.screenshot()

filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

screenshot.save(filename)

print(f"✅ Screenshot saved as {filename}")
