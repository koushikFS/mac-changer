import subprocess
import optparse
import re


def get_arguments():
    arguments = optparse.OptionParser()
    arguments.add_option("-i", "--interface", metavar='\b', dest="interface", help="interface")
    arguments.add_option("--mac", "-m", metavar='\b', dest="new_mac", help="spoof mac address")
    (values, option) = arguments.parse_args()
    if not (values.interface and values.new_mac):
        arguments.error("give arguments\n[+]HELP: python3 macchanger.py -h")
    return values


def mac_changer(x, y):
    try:
        print("Mac-changer coded by @koushikk11")
        print("[+]changing the mac-address of {a} to {b}".format(a=x, b=y))
        subprocess.call(["ifconfig", x, "down"])
        subprocess.call(["ifconfig", x, "hw", "ether", y])
        subprocess.call(["ifconfig", x, "up"])
    except KeyboardInterrupt:
        print("[+]Quiting...")


def extract():
    ifconfig_result = subprocess.check_output(["ifconfig", values.interface])
    extracted_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if extracted_result:
        return extracted_result.group(0)
    else:
        print("[-]couldn't find any mac address for the given interface")
        exit()


def check(o, n):
    if o == n:
        print("[-]ur mac address is not changed")
        permanant_mac(values.interface)
        print("old mac:           {}".format(o))
        print("new mac:           {}".format(n))

    else:
        print("[+]your mac address is successfully changed")
        permanant_mac(values.interface)
        print("old mac = {}".format(o))
        print("new mac = {}".format(n))


def permanant_mac(interface):
    subprocess.run("ethtool -P "+interface, shell=True)


values = get_arguments()
old_mac = extract()
mac_changer(values.interface, values.new_mac)
new_mac = extract()
check(old_mac, new_mac)
# print(used_macs[0])
