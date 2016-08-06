import socket, ssl
from Config import *

def open_socket():
  s = socket.socket()
  s.connect((HOST, PORT))
  s = ssl.wrap_socket(s)
  s.send(("PASS " + PASS + "\r\n").encode('UTF-8'))
  s.send(("NICK " + USER + "\r\n").encode('UTF-8'))
  s.send(("JOIN #" + ROOM + "\r\n").encode('UTF-8'))
  return s

def send_message(s, message):
  """Sends message using the socket

  @s is the socket
  @message is the message you want to send
  """
  message_temp = "PRIVMSG #" + ROOM + " :" + message
  s.send((message_temp + "\r\n").encode('UTF-8'))
  print("Sent: " + message_temp)

def send_pong(s, message):
  s.send(("PONG" + message).encode('UTF-8'))
  print("Sent: " + "PONG" + message)
  
def join_room(s):
  """
  Recieves and reads the buffers. Sends the initialization message
  
  @s is the socket
  """
  loading = True
  while(loading):
    response = s.recv(1024).decode('UTF-8')
    temp = response.split("\n")
    response = temp.pop()

    for line in temp:
      print(line)
      loading = loading_complete(line)  
  send_message(s, INITIALIZATION_MESSAGE)

def loading_complete(line):
  if("/NAMES" in line):
    return False
  else:
    return True
  
def get_user_message(text):
  """ Returns the a list containing the user and the message

  @text is the whole text
  """
  pass
