import pywifi
from pywifi import const
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  

    iface.scan()  
    time.sleep(2)  

    results = iface.scan_results()
    
    print(f"{'SSID':30} {'Signal (dBm)':15} {'Security'}")
    print("-" * 60)
    for network in results:
        ssid = network.ssid
        signal = network.signal
        auth = get_auth_type(network.akm)
        print(f"{ssid:30} {signal:15} {auth}")

def get_auth_type(akm_list):
    if not akm_list:
        return "Open"
    akm = akm_list[0]
    if akm == const.AKM_TYPE_NONE:
        return "Open"
    elif akm == const.AKM_TYPE_WPA:
        return "WPA"
    elif akm == const.AKM_TYPE_WPAPSK:
        return "WPA-PSK"
    elif akm == const.AKM_TYPE_WPA2:
        return "WPA2"
    elif akm == const.AKM_TYPE_WPA2PSK:
        return "WPA2-PSK"
    else:
        return "Unknown"

if __name__ == "__main__":
    print("🔍 Scanning for available Wi-Fi networks...\n")
    scan_wifi()
