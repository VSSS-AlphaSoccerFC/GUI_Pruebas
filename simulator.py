import socket
import numpy as np
import time
from game import Robot, Ball, State

class Simulator:
    def __init__(self, global_state):
        print("NEW SIMULATOR")
        self.global_state = global_state

    def next_step(self):
        for ar in self.global_state.away_robots:
            ar.x += np.random.randint(-3,4)
            ar.y += np.random.randint(-3,4)


# Initial global state
robots_home = [Robot(0, 1, "blue", None, x=10, y=65, yaw=0), Robot(1, 1, "red", None, x=50, y=25, yaw=0), Robot(2, 1, "green", None, x=50, y=105, yaw=0)]
robots_away = [Robot(0, 2, "red", None, x=140, y=65, yaw=180), Robot(1, 2, "pink", None, x=100, y=25, yaw=180), Robot(2, 2, "purple", None, x=100, y=105, yaw=180)]
ball = Ball(75, 65)
global_state = State(robots_home, robots_away, ball)

simulator = Simulator(global_state)


for t in range(0,100):
    print(f"TIME: {t}")
    simulator.global_state.print_field()
    simulator.next_step()
    ## Code to move home robots goes here ###

    ####
    time.sleep(.1)


