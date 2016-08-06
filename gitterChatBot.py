from Socket import *
from Config import *
import time

s = open_socket()
join_room(s)


while(True):
  response = s.recv(1024).decode('UTF-8')
  temp = response.split("\n")
  response = temp.pop()

  for line in temp:
    print(line)
    if line[0:4] == "PING":
      send_pong(s, line[4:])
  
  time.sleep(3)
