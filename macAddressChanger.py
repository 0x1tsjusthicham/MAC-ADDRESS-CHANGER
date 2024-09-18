'''
change it manually in kali
    # ifconfig eth0 down
    # ifconfig eth0 hw ether 00:11:22:33:44:55
    # ifconfig etho0 up
'''

import subprocess


mac_address = "00:11:22:33:44:55"
network_interface = "eth0"

subprocess.call(f"ifconfig {network_interface} down", shell=True)
subprocess.call(f"ifconfig {network_interface} hw ether {mac_address}", shell=True)
subprocess.call(f"ifconfig {network_interface} up", shell=True)

print(f"[+] Changing mac address for {network_interface} to {mac_address}")