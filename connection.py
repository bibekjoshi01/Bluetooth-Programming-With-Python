import bluetooth

print("Searching Bluetooth Devices !")
nearby_devices = bluetooth.discover_devices(lookup_names=True)

# Bluetooth Device listing
print("Found {} devices.".format(len(nearby_devices)))
print("--------------------------------")

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))

print("--------------------------------")

target_device = input("Enter Device Name to Connect !")
target_address = None
for addr, name in nearby_devices:
    if target_device == name:
        target_address = addr
        break

if target_address is not None:
    print ("found target bluetooth device with address ", target_address)
else:
    print ("could not find target bluetooth device nearby")

print("Making Connection")

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
print(sock)
response = sock.connect((target_address, 1))
print(response)
speed_command = b'set speed 50\n'
sock.send(speed_command)

# wait for a response from the device
response = sock.recv(1024)
sock.close()

