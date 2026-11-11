### Bill of Materials (BOM)

| Item | Description / Part Number | Qty | Unit Price (USD) | Buying Link |
| :---: | :--- | :---: | :---: | :--- |
| 1 | ESP32-C3-MINI-1 Module | 1 | $2.10 | [DigiKey](https://www.digikey.com/) / [AliExpress](https://www.aliexpress.com/) |
| 2 | AMS1117-3.3 LDO Voltage Regulator (SOT-223) | 1 | $0.15 | [DigiKey](https://www.digikey.com/) / [LCSC](https://lcsc.com/) |
| 3 | USB Type-C Receptacle (16-pin SMT) | 1 | $0.30 | [LCSC](https://lcsc.com/) / [AliExpress](https://www.aliexpress.com/) |
| 4 | 2-Pin JST-PH / Screw Terminal | 2 | $0.10 | [AliExpress](https://www.aliexpress.com/) |
| 5 | 2N7000 N-Channel MOSFET (SOT-23) | 1 | $0.08 | [DigiKey](https://www.digikey.com/) / [LCSC](https://lcsc.com/) |
| 6 | 5V Active Piezo Buzzer (Through-hole) | 1 | $0.45 | [Amazon](https://www.amazon.com/) / [AliExpress](https://www.aliexpress.com/) |
| 7 | Red LED (0805 SMT) | 1 | $0.02 | [LCSC](https://lcsc.com/) |
| 8 | $330\Omega$ Resistor (0805) | 1 | $0.01 | [DigiKey](https://www.digikey.com/) |
| 9 | $10\mu\text{F}$ Ceramic Capacitor (0805) | 2 | $0.03 | [DigiKey](https://www.digikey.com/) |
| 10 | $0.1\mu\text{F}$ Decoupling Capacitor (0805) | 2 | $0.01 | [DigiKey](https://www.digikey.com/) |
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
