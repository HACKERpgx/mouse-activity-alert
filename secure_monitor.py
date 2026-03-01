"""
Mouse Tamper Monitor
Detects clicks and scrolls → plays alert sound + logs event
Works on Windows, macOS, Linux (sound quality varies)
"""

import time
import datetime
import sys
import platform

try:
    from pynput import mouse
except ImportError:
    print("Error: 'pynput' library not found.")
    print("Install it with:  pip install pynput")
    sys.exit(1)

# ────────────────────────────────────────
# CONFIG
# ────────────────────────────────────────
ALERT_COOLDOWN = 10     # seconds between alerts
BEEP_FREQUENCY = 1800   # Hz (Windows only)
BEEP_DURATION  = 600    # ms  (Windows only)
# ────────────────────────────────────────

last_alert = 0

def play_alert():
    """Cross-platform alert sound (best effort)"""
    sys.stdout.write("\a")          # Terminal bell - works almost everywhere
    sys.stdout.flush()

    if platform.system() == "Windows":
        try:
            import winsound
            winsound.Beep(BEEP_FREQUENCY, BEEP_DURATION)
        except:
            pass  # fallback to \a only

def on_click(x, y, button, pressed):
    global last_alert
    if not pressed:
        return

    now = time.time()
    if now - last_alert < ALERT_COOLDOWN:
        return

    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"[{ts}] ALERT: {button} pressed at ({x}, {y})")
    play_alert()
    print("!!! TAMPER ALERT !!!\n")
    last_alert = now

def on_scroll(x, y, dx, dy):
    global last_alert
    now = time.time()
    if now - last_alert < ALERT_COOLDOWN:
        return

    direction = "up" if dy > 0 else "down"
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"[{ts}] ALERT: Scrolled {direction} at ({x}, {y})")
    play_alert()
    print("!!! TAMPER ALERT !!!\n")
    last_alert = now

# ────────────────────────────────────────
print("Secure Tamper Monitor running...")
print("→ Any mouse click or scroll = ALERT!")
print("→ Press Ctrl+C to stop.\n")

try:
    with mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll,
        # on_move=...  # you can add later if needed
    ) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\nStopped.")
except Exception as e:
    print(f"\nError: {e}")
    sys.exit(1)