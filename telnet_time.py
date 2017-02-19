#import telnetlib
import time
import datetime					#or from datetime import datetime Import just "datetime" module from "datetime" class (cut out the shit)
import socket
import sys
import _thread

def main():
	
	def clientThread(conn):
		# Send a welcome message to new connected clients
		RAWwelcomeMessage = "--- Welcome to the server.\n--- Type some stuff: "
		welcomeMessage = RAWwelcomeMessage.encode("utf-8")
		conn.send(welcomeMessage)														# SEND ONLY
	
		# Infinte loop so that threads do no end or terminate unexpectedly
		while True: 
			# While still data in buffer
			data = conn.recv(1024)
			RAWdata = data.decode("utf-8")
			reply = "From client: " + RAWdata
			print("--- Sending welcome message: " + reply)
			sendWelcome = reply.encode("utf-8")
		
			if not data:
				break
		
			conn.sendall(sendWelcome)
		
		# Come out of loop
		conn.close()
		
	timeNow = time.strftime("%d/%m/%Y %H:%M:%S")
	HOST = '' 

	localAsServer = input("--- Would you like to use MR as server?\n - ")
	if localAsServer is "y":
		hostVar = "54.18.5.0"
		print("[" + timeNow	+ "] Using " + hostVar + " as the host IP.")
	else:
		hostVar = ' '																	# LATER: --> input("--- Enter the IP you would like to use as TCP server:\n - ")
		print("[" + timeNow + "] Using " + hostVar + " as the host IP.")

	Port = 55555																		# LATER: ---> input("--- Enter the port to connect with: ")
	print("--- Using " + str(Port) + " as connection port")
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("----- Socket created.")
	
	# Bind socket to local host port
	try: 
		s.bind((HOST, Port))
	except socket.error as msg:
		print("Bind failed w/ error code: " + str(msg[0]) + " Message: " + msg[1])
		sys.exit()
	print("----- Socket Binding complete")
	
	# Start listening on the created socket
	s.listen(1)
	print("Socket will begin listening.")
	
	# Remain talking (open) to the client
	while 1:
		# Wait to a accept a connection - blocking call
		conn, addr = s.accept()
		print(str(addr) + ":" + str(addr))
		print("Connected to client: " + str(addr[0]) + ":" + str(addr[1]))					# (Type error being thrown when printing connected client info)
	
		# Start new thread. Takes 1st arg as function to be ran (line 39), second is the tuple of arguments to the function.
		_thread.start_new_thread(clientThread,(conn, ))
	
	s.close()
	
	
	
if __name__ == "__main__":
	main()
	
	
	
	
	
	
#	print("\n\n")
#	#time.sleep(.5)	# sleep for <seconds (s)>
#	print("---")
#	#time.sleep(2)
#	print("The time is currently: ")
#	time.sleep(1)
#	
#	now = datetime.datetime.now()
#	print (now)
#	print ("or")
#	print("[" + time.strftime("%d/%m/%Y %H:%M:%S") + "]		<-- This one though right?!")
#	
#	
#	print("---\n")
#	input("press <ENTER> key...")
#	print("...done\n")
