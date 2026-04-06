import tkinter as tk
import pyscreenshot as ImageGrab
import os
import time

# 📸 Function from your image (fixed)
def simple_screenshot():
    img = ImageGrab.grab(backend="mss")
    img.save("/home/aiat/Downloads/screenshot.png")
    print("Saved to Downloads folder")

# 📸 Full screen screenshot (button)
def take_screenshot():
    root.withdraw()
    time.sleep(1)

    img = ImageGrab.grab()
    img.save("screenshot.png")

    print("Screenshot saved as screenshot.png")
    root.deiconify()

# 📸 Capture only app window
def capture_screen():
    try:
        root.withdraw()
        time.sleep(1)

        x = root.winfo_rootx()
        y = root.winfo_rooty()
        w = root.winfo_width()
        h = root.winfo_height()

        print("Capturing:", x, y, w, h)

        img = ImageGrab.grab(bbox=(x, y, x + w, y + h))

        filepath = os.path.join(os.getcwd(), "window_screenshot.png")
        img.save(filepath)

        print("Saved to:", filepath)

    except Exception as e:
        print("ERROR:", e)

    root.deiconify()


# 🖥 GUI
root = tk.Tk()
root.title("Screenshot App")
root.geometry("300x250")

tk.Button(root, text="Full Screenshot", command=take_screenshot).pack(pady=10)
tk.Button(root, text="Window Screenshot", command=capture_screen).pack(pady=10)
tk.Button(root, text="Save to Downloads", command=simple_screenshot).pack(pady=10)
tk.Button(root, text="Cancel", command=root.destroy).pack(pady=10)

root.mainloop()