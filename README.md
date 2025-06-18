# 🔍 Wi-Fi Scanner using Python

This is a simple **Wi-Fi Scanner** built with Python that scans all nearby Wi-Fi networks and displays key information such as SSID, signal strength (in dBm), and security type.

## 📌 Features

* Scans all available Wi-Fi networks
* Displays:

  * 📦 SSID (Wi-Fi name)
  * 📉 Signal strength (in dBm)
  * 🔐 Security type (e.g., WPA2-PSK, Open, etc.)
* Lightweight and terminal-based output

## 💠 Built With

* **Python 3**
* [`pywifi`](https://pypi.org/project/pywifi/): A cross-platform Python module to work with Wi-Fi interfaces
* `time` module (for delay after scanning)

## 📷 Sample Output

```
🔍 Scanning for available Wi-Fi networks...

SSID                           Signal (dBm)    Security
------------------------------------------------------------
Home_Network                   -45             WPA2-PSK
Cafe_WiFi                      -70             Open
Office_5G                      -55             WPA-PSK
```

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your machine
* Wi-Fi interface (enabled)
* Admin/root privileges (recommended)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/wifi-scanner.git
   cd wifi-scanner
   ```

2. Install the required package:

   ```bash
   pip install pywifi
   ```

### Run the Script

```bash
python wifi.py
```

## 📁 File Structure

```
wifi.py        # Main script to scan and display Wi-Fi networks
```

## 🧐 How it Works

* Uses `pywifi` to access your Wi-Fi adapter
* Initiates a scan using `iface.scan()`
* Waits for 2 seconds to let the scan complete
* Fetches results and displays them in a formatted table
* Detects security type using `akm` (authentication key management) protocols

## 🔒 Security Note

This script is **read-only** — it does **not connect to** or **interfere with** any networks.

## 🙌 Acknowledgments

* Thanks to `pywifi` developers for making Wi-Fi interface access in Python easy!
* This project was developed as part of my internship at \[YourCompanyName].

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

---

📧 Feel free to reach out for collaboration or feedback!
