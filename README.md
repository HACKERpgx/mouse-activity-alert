### Bill of Materials (BOM)

| Part Description | Quantity | Unit Price (USD) | Buying Link |
| :--- | :---: | :---: | :--- |
| ESP32 Microcontroller | 1 | $9.26 | [https://www.amazon.ae/HiLetgo-ESP-WROOM-32-Development-Microcontroller-Integrated/dp/B0718T232Z/ref=sr_1_1?crid=3BXWVT42TES2N&dib=eyJ2IjoiMSJ9.zT-HWQXSZP4-EGGQ1xWDN935gcPyTq_zjc3e9kqwgOhlqXcqKKAYLA0SwHTYD2-_KuYhwLMCRbJ0PVt1my1YniWBymduufE5uHrbVQGBC--NgMeZYvrAdL7PQgwNNxCjU9oU9fnt6he7uxW2u8o0w-jGecvZbCK3yW64mEVl_L6_Hl4oEhs7uatVDCyGlzUMpcyQPgfNnjZYDcFXUGedLpsfSlpDNRIr8sxK92ed5y-ZqqgKFoftdHuB0ff_NAH5rXDXlkYqvsMgelP6PQOJWuB67cJGyHtptLlKwfc2JCo.cgdivDamaTJ_c2h4mGXiK6sxsXt8DGpE0VKGGeqceXk&dib_tag=se&keywords=ESP32+Microcontroller&qid=1794405915&sprefix=esp32+microcontroller%2Caps%2C525&sr=8-1] |
| Buzzer / Alarm Module | 1 | $5.44 | [https://www.amazon.ae/Active-Buzzer-Module-Arduino-Compatible/dp/B0H1FH97RJ/ref=sr_1_1?crid=2TDYUXDE1TUG7&dib=eyJ2IjoiMSJ9.Nn4RZJ5BNimv92qw9OqTOGkFTc-Nc6eWlnbFP1T0ekK-DugK4iSNGUvENJx4jsyI2ZHOWQszrNhmY15WuqA8DaoHeFDlPHPajGHC4j2aqDNKiwmxklFqcgS8Gj4v-vqmPEDQzfp9S9xOdXju3d32ldiU8GJN4bJE-8inI0vlK-Xh-Wt7Hn5Kxkemw6l91d7t-D_S-qWHavL7sXbCqp3cEgXKMvHCEB63w6wTJWDE6tjxsitprCDtyPTzJ0PRpzC8D_TNJo_UOZzPKVahzGzC2hfc-X2OnGG3h9unJqDrsS0.lOZOFASNxYI7tPPJnQfsDI-t9H1WUY2g9THkurXORMo&dib_tag=se&keywords=Buzzer+%2F+Alarm+Module&qid=1794406172&sprefix=buzzer+%2F+alarm+module%2Caps%2C354&sr=8-1] |
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
