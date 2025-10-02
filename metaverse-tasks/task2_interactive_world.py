from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# ground
ground = Entity(model='plane', scale=Vec3(10), texture='white_cube', texture_scale=(10,10), collider='box')

# player
player = FirstPersonController()  # WASD + mouse look

# interactive cube
cube = Entity(model='cube', color=color.orange, rotation=Vec3(0, 0, 0), collider='box')

def update():
    if player.intersects(cube).hit:   # check collision
        cube.color = color.random_color()  # change color when touched

app.run()
