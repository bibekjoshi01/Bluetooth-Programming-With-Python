import bluetooth

print("Searching !")
nearby_devices = bluetooth.discover_devices(lookup_names=True)

# Bluetooth Device listing
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))

# address = input('Enter Mac Address')
address =  'D6:5A:F4:DF:74:4E'
# Connect to the airbuds using the address
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((address, 1))
print("Connected !")
# Send a command to the airbuds
command = b'play'
sock.send(command)  

# Receive a response from the airbuds
response = sock.recv(1024)
print(response)

# Close the connection
sock.close()
