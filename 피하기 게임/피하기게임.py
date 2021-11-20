from ursina import *

move = 4

def update():
    if held_keys['a']:
    #물체가 왼쪽으로 이동
       player.x -= move * time.dt

    if held_keys['d']:
    #물체가 오른쪽으로 이동
       player.x += move * time.dt

player = Entity(model = 'quad', color = color.green, position = (0, -4), scale = (0.5,0.5))

app = Ursina()
app.run()
