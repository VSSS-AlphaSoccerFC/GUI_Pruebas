import socket
from object_pb2 import ObjectData

class Robot:
    def __init__(self, rid=0, team=1, color=None, sock=None, x=0, y=0, yaw=0):
        self.id = rid
        self.team = team
        self.color = color
        self.x = x
        self.y = y
        self.yaw = yaw
        self.socket = sock
    
    def set_socket(sock):
        self.socket = sock


class Ball:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class State:
    def __init__(self, home_robots=[], away_robots=[], ball=Ball(75, 65)):
        """
            Global state of the match
        """
        
        self.home_robots = home_robots
        self.away_robots = away_robots
        self.ball = ball
        self.field = Field(150, 130)

        self.status = 0
        self.home_goals = 0
        self.away_goals = 0

    def print_field(self):
        frac = 7
        print((self.field.width//frac)*"-")
        for i in range(self.field.height//frac+5):
            for j in range(self.field.width//frac+1):
                if j == 0 or j == self.field.width//frac:
                    print(".", end="")
                else:
                    found = False
                    for hr in self.home_robots:
                        if hr.x//frac == i and hr.y//frac == j:
                            print("o",end="")
                            found = True
                    
                    if self.ball.x//frac == i and self.ball.y//frac == j:
                        print("@",end="")
                        found = True
                        
                    for ar in self.away_robots:
                        if ar.x//frac == i and ar.y//frac == j:
                            print("x",end="")
                            found = True
                    
                    if not found:
                        print(" ", end="")

            print("")
        print((self.field.width//frac)*"-")


    def update(self, serialized):
        """
        serialized: serialized data from protobuffer.SerializeToString()
        """
        deserialized = ObjectData()
        deserialized.ParseFromString(serialized)
        print(deserialized.id)
        if deserialized.kind == 1:
            # Robot
            if deserialized.team == 1:
                self.home_robots[deserialized.id].x = deserialized.x
                self.home_robots[deserialized.id].y = deserialized.y
                self.home_robots[deserialized.id].yaw = deserialized.yaw
                self.home_robots[deserialized.id].team = deserialized.team
            
            elif deserialized.team == 2:
                self.away_robots[deserialized.id].x = deserialized.x
                self.away_robots[deserialized.id].y = deserialized.y
                self.away_robots[deserialized.id].yaw = deserialized.yaw
                self.away_robots[deserialized.id].team = deserialized.team

        elif deserialized.kind == 2:
            self.ball.x = deserialized.x
            self.ball.y = deserialized.y
