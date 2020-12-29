import ipaddress

x = []


def is_ipv4():
    while True:
        ip_address = str(input("Enter IP address (Type x to End): "))
        try:
            ipaddress.IPv4Address(ip_address)
            print(str(ip_address) + " is a valid IP address")
        except ValueError:
            if (str(ip_address) == "x"):
                break
            else:
                print(str(ip_address) + " is not a valid IP Address")
            return ip_address


is_ipv4()
