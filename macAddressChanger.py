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
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="network_interface", help="this place for network interfaces")
    parser.add_option("-m", "--mac", dest="new_mac", help="this place for mac addresse")
    options, arguments = parser.parse_args()

    #print(options)

    if not options.network_interface:
        parser.error("[-] You forgot to put network interface, type -h or --help for help")
        exit()
    if not options.new_mac:
        parser.error("[-] You forgot to put new mac, type -h or --help for help")
        exit()

    return options


# they are a system commands that change mac address for network interface
def mac_changer(network_interface, new_mac):
    subprocess.call(f"ifconfig {network_interface} down", shell=True)
    subprocess.call(f"ifconfig {network_interface} hw ether {new_mac}", shell=True)
    subprocess.call(f"ifconfig {network_interface} up", shell=True)

    print(f"[+] Changing mac address for {network_interface} to {new_mac}")


# filtering mac address
def get_mac(network_interface):
    ifconfig_result = subprocess.check_output(f"ifconfig {network_interface}").decode("UTF-8")
    mac_address = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    return mac_address[0]


options = get_arguments(network_interface, new_mac)
mac_changer(options.network_interface, options.new_mac)
mac_address = get_mac(options.network_interface)
if mac_address == options.new_mac:
    print("MAC changed successfully")
else:
    print("Something went wrong")