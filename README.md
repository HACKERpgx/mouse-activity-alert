
# Mouse Tamper Monitor

A simple, lightweight Python script that **detects unauthorized mouse activity** (clicks or scrolling) and plays an audible + visual alert.

Useful for:
- Monitoring unattended computers  
- Detecting physical tampering / shoulder surfing  
- Quick DIY security prototype  
- Educational purposes (global input hooks)

**Important**: This is **not** a production-grade security tool. It can be bypassed (e.g., killing the Python process, suspending the machine, using virtual machines, etc.).

## Features

- Real-time detection of **left/right/middle clicks** and **scrolling**  
- Audible alert (platform-aware) + console message  
- Cooldown between alerts (prevents spam)  
- Clean exit with Ctrl+C  
- Minimal dependencies
- Any mouse click or scroll → beep + alert message
- Alerts are suppressed for 10 seconds after each trigger (configurable)

**Example output**
Secure Tamper Monitor running... Any button press or scroll = ALERT!

Press Ctrl+C to stop.

[2026-03-01 16:45:12.337] ALERT: Button.left pressed at (842, 619)

!!! TAMPER ALERT !!!

[2026-03-01 16:45:25.114] ALERT: Scrolled down at (842, 619)

!!! TAMPER ALERT !!!

^C

Stopped.

<img width="772" height="562" alt="running secure_monitor" src="https://github.com/user-attachments/assets/cb4005f6-3f0b-40e9-b0ee-6f047be49baf" />
<img width="552" height="440" alt="Tamper alert logs" src="https://github.com/user-attachments/assets/46474713-7faa-4753-a172-1669e6a5cea6" />

**License**

MIT License – feel free to use, modify, distribute.

## Requirements

- Python 3.6+  
- `pynput` (only external dependency)

```bash
pip install pynput
python secure_monitor.py
