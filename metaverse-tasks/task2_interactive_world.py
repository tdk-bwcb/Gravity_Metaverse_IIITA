from ursina import Ursina, Entity, Vec3, Vec2, color, held_keys
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Ground
ground = Entity(
    model='plane',
    scale=Vec3(10, 1, 10),          # Vec3 requires 3 values
    texture='white_cube',
    texture_scale=Vec2(10, 10),     # Use Vec2 for texture_scale
    collider='box'
)

# Player
player = FirstPersonController()  # WASD + mouse look

# Interactive cube
cube = Entity(
    model='cube',
    color=color.orange,
    rotation=Vec3(0, 0, 0),
    collider='box'
)

def update():
    if player.intersects(cube).hit:  # Check collision
        cube.color = color.random_color()  # Change color when touched

app.run()
