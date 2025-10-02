from ursina import *

app = Ursina()

DirectionalLight().look_at(Vec3(1,-1,-1))  # basic lighting
EditorCamera()  # free camera controls with right mouse

ground = Entity(model='plane', scale=15, texture='white_cube', texture_scale=(15,15), collider='box')

player = FirstPersonController()

# interactive objects
door = Entity(model='cube', color=color.brown, position=(3,1,3), scale=(1,2,0.1), collider='box')
rotating_cube = Entity(model='cube', color=color.azure, position=(-2,1,-2), collider='box')

door_open = False

def update():
    global door_open
    if held_keys['e'] and distance(player.position, door.position) < 2:
        if not door_open:
            door.position += Vec3(0,2,0)   # move up = open
            door_open = True
        else:
            door.position -= Vec3(0,2,0)   # move down = close
            door_open = False
    
    if player.intersects(rotating_cube).hit:
        rotating_cube.rotation_y += 2  # rotate when touched

app.run()
