import getpass
import telnetlib

HOST = "192.168.122.72"
user = input("Enter your telnet username ")
password = getpass.getpass()

telnet = telnetlib.Telnet(HOST)

telnet.read_until(b"Username: ")
telnet.write(user.encode('ascii') + b"\n")
if password:
    telnet.read_until(b"Password: ")
    telnet.write(password.encode('ascii') + b"\n")

telnet.write(b"enable\n")
telnet.write(b"cisco\n")
telnet.write(b"conf t\n")

for x in range(2,20):
    telnet.write(b"vlan " + str(x).encode('ascii') + b"\n")
    telnet.write(b"name VLAN_" + str(x).encode('ascii') + b"\n")


telnet.write(b"end\n")
telnet.write(b"exit\n")

print(telnet.read_all().decode('ascii'))

