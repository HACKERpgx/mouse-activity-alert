"""
Mouse Tamper Monitor with Threaded Voice Alerts
Detects clicks and scrolls -> queues speech + logs event without blocking
"""
import sys
import time
import queue
import threading
from datetime import datetime
from pynput import mouse

try:
    import pyttsx3
except ImportError:
    print("Error: 'pyttsx3' library not found.")
    print("Install it with: py -m pip install pyttsx3 pynput")
    sys.exit(1)

# Thread-safe speech queue
speech_queue = queue.Queue()

def tts_worker():
    """Dedicated background thread for pyttsx3 to prevent blocking and COM errors."""
    try:
        engine = pyttsx3.init()
    except Exception as e:
        print(f"TTS Init Error: {e}")
        return

    while True:
        message = speech_queue.get()
        if message is None:
            break
        try:
            engine.say(message)
            engine.runAndWait()
        except Exception as e:
            print(f"TTS Speech Error: {e}")
        finally:
            speech_queue.task_done()

# Start background speech thread
worker_thread = threading.Thread(target=tts_worker, daemon=True)
worker_thread.start()

# CONFIG
ALERT_COOLDOWN = 3  # seconds between voice alerts
last_alert = 0

def speak_alert(message):
    speech_queue.put(message)

def on_click(x, y, button, pressed):
    global last_alert
    if not pressed:
        return

    now = time.time()
    if now - last_alert < ALERT_COOLDOWN:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    
    if button == mouse.Button.left:
        msg = "Left mouse button triggered! Tamper alert!"
    elif button == mouse.Button.right:
        msg = "Right mouse button clicked! Security breach!"
    else:
        msg = f"Mouse button pressed at ({x}, {y})"

    print(f"[{timestamp}] ALERT: {msg}")
    speak_alert(msg)
    last_alert = now

def on_scroll(x, y, dx, dy):
    global last_alert
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
print("Secure Tamper Monitor with Threaded Voice Active...")
print("→ Any mouse click or scroll will speak an alert!")
print("→ Press Ctrl+C to stop.\n")

try:
    with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\nStopped.")
    speech_queue.put(None)
except Exception as e:
    print(f"\nError: {e}")
    sys.exit(1)
