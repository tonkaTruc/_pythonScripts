import telnetlib
import sys
import time
import sys
import socket
from curses.ascii import ctrl

def main():

# Telnet protocol characters (don't change)
	IAC  = chr(255) # "Interpret As Command"
	DONT = chr(254)
	DO   = chr(253)
	WONT = chr(252)
	WILL = chr(251)
	theNULL = chr(0)
	LINEMODE = chr(34) 			# Linemode option

	#HOST="localhost"
	HOST ='54.18.5.0'
	PORT=55555

	modeChar="\ff\fd\03\ff\fd\01"

# Print out variables to be used when connecting
	print('------------------------------------ Connection variables:')
	print('HOST:' + HOST)
	print('PORT: ' + str(PORT))

# Make the connection and read back to client terminal
	print('------------------------------------ Making connection:')
# creating new socket
	tn=telnetlib.Telnet(HOST, PORT, timeout = 1)
	print("----- Socket created.")
	
 # Connect to remote host socket + host port
	try: 
		tn.sock.send(telnetlib.IAC + telnetlib.WONT + telnetlib.LINEMODE)
		time.sleep(1)
	except socket.error as msg:
		print("Connection failed w/ error code: " + str(msg[0]) + " Message: " + msg[1])
		sys.exit()
	print("----- Socket connection complete")
	print("----- Send data over socket to: " + HOST + ":" + str(PORT) + "\n")
	
	COMMAND="siop 100".encode('utf-8')
	print('Sending ' + str(COMMAND) + " to telnet...\n")
	tn.write(COMMAND + b'\r')
	time.sleep(1)	
	RESULT=tn.read_very_eager().decode('utf-8')
	print(RESULT)
	
	print('\n------------------------------------ Connection established:')

	print('closing socket')
	tn.close()
#	s.close()






	#while 1 
	#tn.write(ESC)
	#tn.write(MODE.encode("hex"))
	#tmp = tn.read_very_eager().decode('utf-8')
	#print("Remote msg is: " + tmp)
	
	#print("Telnet addr is: " + str(tn))

	#tn.write("Hello from python...\n")
	#print('First read :\n')
	#print tn.read_eager()
	#time.sleep(10)
	#print('Second read :\n')
	#print tn.read_eager()
	print('-------- EOF')

#tn.sock.send(telnetlib.IAC+telnetlib.DO)
#data=tn.sock.recv(1024)
#if not data:
	#print('----- GOT NO DATA!')
#else:
	#print('got data!!!\n')
	#print(str(data))
	
#tn.write("db 118\n")
#tn.write("ls\n")
#tn.write("exit\n")
#print tn.read_all()

if __name__ == "__main__":
		main()
