'''
change it manually in kali
    # ifconfig eth0 down
    # ifconfig eth0 hw ether 00:11:22:33:44:55
    # ifconfig etho0 up
'''

import subprocess
import optparse
import re

# this is a reader that will take mac address and network interface
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="network_interface", help="this place for network interfaces")
parser.add_option("-m", "--mac", dest="new_mac", help="this place for mac addresse")
options, arguments = parser.parse_args()

#print(options)

if not options.network_interface:
    print("[-] You forgot to put network interface")
    exit()
if not options.new_mac:
    print("[-] You forgot to put new mac")
    exit()

# they are a system commands that change mac address for network interface
subprocess.call(f"ifconfig {options.network_interface} down", shell=True)
subprocess.call(f"ifconfig {options.network_interface} hw ether {options.new_mac}", shell=True)
subprocess.call(f"ifconfig {options.network_interface} up", shell=True)

print(f"[+] Changing mac address for {options.network_interface} to {options.new_mac}")

# filtering mac address
ifconfig_result = subprocess.check_output(f"ifconfig {options.network_interface}").decode("UTF-8")
mac_address = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

if mac_address[0] == options.new_mac:
    print("MAC changed successfully")
else:
    print("Something went wrong")