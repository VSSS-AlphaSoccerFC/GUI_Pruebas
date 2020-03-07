from object_pb2 import ObjectData
import socket
import time
from random import randint

s = socket.socket()
s.connect(('192.168.1.72', 4000))
i = 0

while True:
    ball = ObjectData()
    ball.kind = 2
    ball.id = -1
    ball.x = randint(0,1000)
    ball.y = randint(0,1000)
    s.sendall(ball.SerializeToString())
    time.sleep(.1)
   
    for i in range(6):
        y = ObjectData()
        y.kind = 1
        y.id = i%3
        y.team = (i//3)+1
        y.x = randint(0,1000)
        y.y = randint(0,1000)
        if i > 2:
            y.yaw = randint(0,361)
        print(y.SerializeToString())
        time.sleep(.1)
        s.sendall(y.SerializeToString())

    time.sleep(.1)
