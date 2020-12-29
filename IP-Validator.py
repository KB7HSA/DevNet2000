import ipaddress
import sys
import traceback


def Main(args):
    try:
        continueLoop = True
        while continueLoop:
            # Getting IP Address
            ipAddr = input("Enter IP Address (Type x to End):")

            # cleaning white space
            ipAddress = ipAddr.rstrip()

            if (ipAddress.capitalize() == 'X'):
                continueLoop = False
            elif (validateIPAddress(ipAddrress)):
                print(ipAddress + " is a Valid IP Address!")
            else:
                print(ipAddress + " is NOT a valid IP Address!")
        return (0)

    except Exception as X:
        print(X)
        raise (traceback.format_exc())

    finally:
        print("Cisco Systems, Inc (c) (2020)")


def validateIPAddress(ip="127.0.0.1"):
    try:
        ip_addr = ipaddress.ip_address(ip)
    except Exception:
        return False
    return (True)


# Useage
def useage():
    print(sys.argv[0])

if (__name__ == '__main__'):
    sys.exit(Main(sys.argv[1:]))
