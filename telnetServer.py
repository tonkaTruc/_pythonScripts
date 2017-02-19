#import telnetlib
import time
import datetime					#or from datetime import datetime Import just "datetime" module from "datetime" class (cut out the shit)
import socket
import sys
import _thread

def main():

	timeNow = time.strftime("%d/%m/%Y %H:%M:%S")
	HOST = '127.0.0.1' 
	
	def clientThread(conn):
		# Send a welcome message to new connected clients
		conn.send(str("--- Welcome to the server. Type some stuff: \n").encode("utf-8"))													# SEND ONLY
		# conn.send(str("Connected to server as: " + str(conn[0]) + ": " + str(conn[1]) + " \n ").encode("utf-8"))
		# Infinte loop so that threads do no end or terminate unexpectedly
		while True: 
			# While still data in buffer
			try:
				print("--- No ecode error")
				data = conn.recv(1024).decode("utf-8")
			except UnicodeDecodeError as errOP:
				print("[ " + timeNow + " ] Got DECODE error. You must be running windows?... try again...")
				print("[" + timeNow + "] " + str(conn.recv))
				data = str(conn.recv(1024))
			
			if not data:
				print("-------------------- Connection to client: <" + str(addr) + "> has been lost")
				break
				sys.exit()
			print("[" + timeNow + "] " "Reply sent to client: " + "\"We got your message <" + str(data) + "> ...now fuck off!\"\n")
			
			reply = str("We got your message <" + str(data) + "> ...now fuck off!\n").encode("utf-8")
			conn.sendall(reply)
		
		# Come out of loop
		conn.close()

	localAsServer = input("--- Would you like to use MR as server?\n - ")
	if localAsServer is "y":
		hostVar = "54.18.5.0"
		print("[" + timeNow	+ "] Using " + hostVar + " as the host IP.")
	else:
		hostVar = ' '																	# LATER: --> input("--- Enter the IP you would like to use as TCP server:\n - ")
		print("[" + timeNow + "] Using localhost: " + HOST + " as the host IP.")

	Port = 55555																		# LATER: ---> input("--- Enter the port to connect with: ")
	print("--- Using " + str(Port) + " as connection port")
	
	#Define the socket
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
	print("----- Socket will begin listening.\n")
	
	# Remain talking (open) to the client
	while 1:
		# Wait to a accept a connection - blocking call
		conn, addr = s.accept()
		print("Connection from client: " + str(addr[0]) + ":" + str(addr[1]) + "\n")					# (Type error being thrown when printing connected client info)
		print("-\n")
		print("-\n")
		print("-\n")
		print("\"Conn\" variable = " + str(conn))
		print("\"addr\" variable = " + str(addr))
		print("-\n")
		print("-\n")
		print("-\n")
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
