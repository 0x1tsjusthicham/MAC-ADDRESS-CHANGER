'''
change it manually in kali
    # ifconfig eth0 down
    # ifconfig eth0 hw ether 00:11:22:33:44:55
    # ifconfig etho0 up
'''

import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig etho0 up", shell=True)