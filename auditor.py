import subprocess
import os
import sys

def check_root():
    if os.geteuid() != 0:
        print("[-] Error: This script must be run with sudo.")
        sys.exit(1)

def get_interfaces():
    print("[*] Checking for wireless interfaces...")
    try:
        output = subprocess.check_output("iw dev | grep Interface", shell=True).decode()
        return [line.split()[1] for line in output.split('\n') if line]
    except:
        return []

def start_monitor_mode(iface):
    print(f"[*] Putting {iface} into monitor mode...")
    subprocess.run(f"sudo airmon-ng start {iface}", shell=True, check=True)

def main():
    check_root()
    interfaces = get_interfaces()
    if not interfaces: return
    print(f"Available: {', '.join(interfaces)}")
    target = input("Select interface: ")
    if target in interfaces:
        start_monitor_mode(target)
        print("[+] Success!")

if __name__ == "__main__":
    main()
