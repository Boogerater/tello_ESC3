
from djitellopy import tello
from time import sleep

so = tello.Tello()
so.hi()

print(so.get_battery())
