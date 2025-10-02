from ursina import *

app = Ursina()

cube = Entity(model='cube', color=color.azure, rotation=(0,0,0))

def update():
    cube.rotation_y += 1   # rotates 1 degree per frame

app.run()
