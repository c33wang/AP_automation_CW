import socket
 
PORT = 8080



def play_youtube(ip,num):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, PORT))
    sock.sendall(num + "\n")

play_youtube("192.168.5.1", "two")
play_youtube("192.168.5.2", "two")
play_youtube("192.168.5.3", "two")
play_youtube("192.168.5.4", "two")
play_youtube("192.168.5.5", "two")
play_youtube("192.168.5.6", "two")








# data = sock.recv(1024)
# print "1)", data
#
# if ( data == "olleH\n" ):
#     sock.sendall("Bye\n")
#     data = sock.recv(1024)
#     print "2)", data
#
#     if (data == "eyB}\n"):
#         sock.close()
#         printhreet "Socket closed"