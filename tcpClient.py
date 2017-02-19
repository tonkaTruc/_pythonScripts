import socket

def main():
	host = "127.0.0.1"
	port = 5000
	
	s = socket.socket()
	s.connect((host, port))
	
	#debugMessage = message.decode("utf-8")
	#print ("Sending " + str(debugMessage))
	quit = "x"
	
	while quit != "q":
		message = input("-> ").encode("utf-8")		# Ask user to enter text / store in variable "message" / pass "message" variable > ".encode function for # byte format
		if not message:
			break
		s.send(message)
		data = s.recv(1024).decode("utf-8")			# Recive byte variable back from server and decode to string
		print("Received from server: 				" + str(data))
		print("--------------------------\n")
		quit = message.decode("utf-8")
	s.close
	
if __name__ == "__main__":
	main()