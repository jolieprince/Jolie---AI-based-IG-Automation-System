import scrcpy
client = scrcpy.Client("192.168.1.177:5555")
client.start(threaded=True)