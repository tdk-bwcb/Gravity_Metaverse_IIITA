from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import time

app = Ursina()

# Lighting and camera
DirectionalLight().look_at(Vec3(1, -1, -1))
EditorCamera()  # Free camera controls with right mouse

# Ground
ground = Entity(
    model='plane',
    scale=Vec3(15, 1, 15),
    texture='white_cube',
    texture_scale=Vec2(15, 15),  # Vec2 for texture_scale
    collider='box'
)

# Player
player = FirstPersonController()

# Interactive objects
door = Entity(
    model='cube',
    color=color.brown,
    position=Vec3(3, 1, 3),
    scale=Vec3(1, 2, 0.1),
    collider='box'
)

rotating_cube = Entity(
    model='cube',
    color=color.azure,
    position=Vec3(-2, 1, -2),
    collider='box'
)

door_open = False
door_target_y = door.y
door_speed = 4  # units per second

def update():
    global door_open, door_target_y

    dt = time.dt  # type: ignore  # Use Ursina's dt for smooth interpolation

    # Smooth door open/close
    if getattr(held_keys, 'e', False):  # type: ignore
        if distance(player.position, door.position) < 2:
            if not door_open:
                door_target_y = door.y + 2
                door_open = True
            else:
                door_target_y = door.y - 2
                door_open = False

    # Interpolate door position smoothly
    door.y = lerp(door.y, door_target_y, dt * door_speed)

    # Rotate cube when player touches it
    if player.intersects(rotating_cube).hit:
        rotating_cube.rotation_y += 2

app.run()
