"""block_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import *

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 1
block = robot.getDevice('block_connect')
# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    block.lock()
    pass

# Enter here exit cleanup code.
