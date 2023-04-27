import webbrowser
import threading

def locationsPages(target):
	webbrowser.open(target)

for i in range(1000):
	threading.Thread(target = locationsPages, args=["https://xnxx.com"]).start()