
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

## Requirements

- Python 3.6+  
- `pynput` (only external dependency)

```bash
pip install pynput
