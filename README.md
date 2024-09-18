
# MAC Address Changer

This Python script allows you to change the MAC address of a network interface in Kali Linux. It provides an automated way to execute the manual commands used to bring the network interface down, change the MAC address, and bring it back up.

## Manual MAC Address Change (Kali Linux)
The script automates the following manual commands:
```bash
# ifconfig eth0 down
# ifconfig eth0 hw ether 00:11:22:33:44:55
# ifconfig eth0 up
```

## How It Works
- The script takes two inputs from the user:
  1. The network interface (e.g., `eth0`, `wlan0`, etc.)
  2. The new MAC address you want to assign.
  
- It then runs system commands to:
  1. Bring the network interface down.
  2. Change the MAC address.
  3. Bring the interface back up.
  
- It verifies that the MAC address has been changed successfully by retrieving the new MAC address and comparing it to the user input.

## Prerequisites
Make sure you have:
- Python installed (`Python 3.x`)
- Root privileges to execute system commands like `ifconfig`

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/0x1tsjusthicham/MAC-ADDRESS-CHANGER.git
   cd MAC-ADDRESS-CHANGER
   ```

2. **Run the script**:
   To change your MAC address, use the following command:
   ```bash
   sudo python3 mac_changer.py -i [interface] -m [new_mac_address]
   ```
   Replace `[interface]` with your network interface (e.g., `eth0`, `wlan0`), and `[new_mac_address]` with the desired MAC address (e.g., `00:11:22:33:44:55`).

### Example:
```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

This will change the MAC address of the `eth0` interface to `00:11:22:33:44:55`.

## Options
- `-i`, `--interface`: The network interface whose MAC address you want to change.
- `-m`, `--mac`: The new MAC address you want to set.

### Help
You can display help by running:
```bash
python3 mac_changer.py -h
```

## Code Overview

1. **`get_arguments()`**: This function uses `optparse` to parse command-line arguments (interface and MAC address).
2. **`mac_changer()`**: This function changes the MAC address by executing `ifconfig` commands to bring the network interface down, change the MAC address, and bring it up again.
3. **`get_mac()`**: This function retrieves the current MAC address of the specified network interface to verify the change.

## Error Handling
- The script checks if the network interface and MAC address are provided as arguments. If not, it will display an error message and exit.
- After changing the MAC address, it verifies the change by comparing the current MAC address with the new one.

## Notes
- This script is designed for **Kali Linux** and may require adjustments for other Linux distributions.
- The `ifconfig` command is deprecated in some systems in favor of `ip` commands, but it is still widely used in Kali.

## License
@itsjusthicham
