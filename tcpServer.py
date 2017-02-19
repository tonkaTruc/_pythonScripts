import socket
import telnetlib
import time

def Main():

	localAsServer = input("\n\n--- Would you like to use \"localhost\" as server?\n")
	if localAsServer is "y":
		print("Using \"127.0.0.1\" as the host IP.")
		host = "127.0.0.1"
	else:
		print("User defined host IP:")
		host = input("Enter the IP you would like to use as TCP server:\n")
		

	port = 5000
	
	s = socket.socket()
	s.bind((host, port))

	s.listen(1) 													#Listen for one connection at a time
	c, addr = s.accept()
	# DEBUG: print("FROM HERE ---> " + str(c) + str(addr) + " |--- TO HERE!!")
	
	print ("\nconnection from: " + str(addr))
	while True:
		receivedData = c.recv(1024).decode("utf-8")
		#decodedData = receivedData.decode("utf-8")					# Decode the incoming "byteMessage" variable (on client side)
		if not receivedData:          								#end connection if no data in buffer
			break
		print ("[" + time.strftime("%d/%m/%Y %H:%M:%S") + "] - " + "from connected user: " + str(receivedData))
		encodedData = str(receivedData).upper()    				#. to upper method to captilise
		print ("sending : " + str(encodedData))
		encodedData = encodedData.encode("utf-8")
		c.send(encodedData)
	c.close()

if __name__ == '__main__':
    Main()

	
	
	
	
	
#print ("hello world!")
#usrName = input("What is your name?\n")
#print ("Your name is " + usrName + "\n")

#print ("I can count to 10... want me to show you?")
#usrAnswer = input()
#if usrAnswer == 'yes':
#    i = 1
#    while i < 11:
#        print (i)
#        i += 1
#else:
#    print("okay :(")
#print()

#array = ["Shut", "the", "fuck", "up"]
#for a in array:
#   print(a)
 