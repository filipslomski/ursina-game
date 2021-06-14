from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, scale_y=2)

ground = Entity(
    model='cube',
    color=color.magenta,
    z=-.1,
    y=-3,
    origin=(0, .5),
    scale=(50, 1, 10),
    collider='box'
)


def update():   # update gets automatically called.
    player.x += held_keys['d'] * .1
    player.x -= held_keys['a'] * .1


def input(key):
    if key == 'space':
        player.y += 3
        for i in range(1, 3):
            invoke(setattr, player, 'y', player.y-1, delay=.25)


app.run()   # opens a window and starts the game.
