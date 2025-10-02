from ursina import *

app = Ursina()

# ground
ground = Entity(model='plane', scale=10, texture='white_cube', texture_scale=(10,10), collider='box')

# player
player = FirstPersonController()  # comes with WASD controls + gravity

# interactive cube
cube = Entity(model='cube', color=color.orange, position=(2,0.5,2), collider='box')

def update():
    if player.intersects(cube).hit:   # check collision
        cube.color = color.random_color()  # change color when touched

app.run()
