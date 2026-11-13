"""
Mouse Tamper Monitor with Voice Alerts
Detects clicks and scrolls -> speaks alert + logs event
"""
import sys
import platform
from datetime import datetime
from pynput import mouse

try:
    import pyttsx3
except ImportError:
    print("Error: 'pyttsx3' library not found.")
    print("Install it with: pip install pyttsx3")
    sys.exit(1)

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# CONFIG
ALERT_COOLDOWN = 5  # seconds between voice alerts

last_alert = 0

def speak_alert(message):
    print(message)
    try:
        engine.say(message)
        engine.runAndWait()
    except Exception as e:
        print(f"TTS Error: {e}")

def on_click(x, y, button, pressed):
    global last_alert
    if not pressed:
        return

    import time
    now = time.time()
    if now - last_alert < ALERT_COOLDOWN:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    
    if button == mouse.Button.left:
        msg = f"Left mouse button triggered! Tamper alert!"
    elif button == mouse.Button.right:
        msg = f"Right mouse button clicked! Security breach!"
    else:
        msg = f"Mouse button pressed at ({x}, {y})"

    print(f"[{timestamp}] ALERT: {msg}")
    speak_alert(msg)
    last_alert = now

def on_scroll(x, y, dx, dy):
    global last_alert
    import time
    now = time.time()
    if now - last_alert < ALERT_COOLDOWN:
        return

    direction = "up" if dy > 0 else "down"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    msg = f"Mouse scroll {direction} detected! Tamper alert!"
    
    print(f"[{timestamp}] ALERT: {msg}")
    speak_alert(msg)
    last_alert = now

# ────────────────────────────────────────
print("Secure Tamper Monitor with Voice Active...")
print("→ Any mouse click or scroll will speak an alert!")
print("→ Press Ctrl+C to stop.\n")

try:
    with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\nStopped.")
except Exception as e:
    print(f"\nError: {e}")
    sys.exit(1)
