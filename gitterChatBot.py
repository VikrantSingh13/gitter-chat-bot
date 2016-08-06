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

    #Pong the server when needed
    if line[0:4] == "PING":
      send_pong(s, line[4:])
      break

    #extract the user and message from the response line
    temp_message = get_user_message(line)
    user = temp_message[0]
    message = temp_message[1]

    if TARGET_MESSAGE in message:
      send_message(s, "@" + user + " " + REPLY_MESSAGE)
  time.sleep(0.3)
