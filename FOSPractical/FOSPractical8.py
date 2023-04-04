Mutex = True
Full = 0
Empty = 5
Total = 5

def Buffer(Process):
	global Mutex
	global Full
	global Empty
	if Process == 1:
		if Mutex and (Full + Empty == Total) and Full < Total:
			Mutex = False
			Full = Full + 1
			Empty = Empty - 1
			print("Producer is Running.")
			Mutex = True
		elif Mutex == False:
			print("Another Process Exists.")
		elif Full == Total or Empty == 0:
			print("Memory Full.")
	elif Process == 2:
		if Mutex and (Full + Empty == Total) and Empty < Total:
			Mutex = False
			Full = Full - 1
			Empty = Empty + 1
			print("Consumer is Running")
			Mutex = True
		elif Mutex == False:
			print("Another Process Exists")
		elif Full == 0 or Empty == Total:
			print("Memory Empty")

for i in range(6):
	Buffer(1)

for i in range(6):
    Buffer(2)
