from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

colors = [color.green, color.brown]

app = Ursina()

player = FirstPersonController()

ground_particle = Entity(
    model='cube',
    color=color.green,
    z=-.1,
    y=-3,
    origin=(0, .5),
    scale=(100, 5, 100),
    collider='box',
    texture="heightmap_1"
)

#e = Entity(model=Terrain('heightmap_1', skip=12), scale=(200,16,200), texture='heightmap_1', collider='mesh')

def update():   # update gets automatically called.
    pass


def input(key):
    pass


app.run()   # opens a window and starts the game.
