import resources
import pyglet
from GameObjects import PlayerObject
from MinionObjects import Cowboy, Blob
from pyglet.window import key
from Time import Timer
from shoot import hit_cowboy, hit_blob
from pyglet.window import mouse
import sys


# Window setting
window = pyglet.window.Window(width=1200, height=900, caption="DOPE Pen-queen", resizable=False)
window.set_location(400, 100)
frame_rate = 1/16


# Make background
global background_sprite
background = pyglet.resource.image('battleback1.png')
background.width = 1200
background.height = 900
background_sprite = pyglet.sprite.Sprite(img=background, x=0, y=0)

# Create player
player = PlayerObject(600, 0, "main2.png")

# Game settings
character_speed = 5.0
spawn_speed = 4  # seconds

# Cowboy handle
cowboys = []
number = 2
cowboyBatch = pyglet.graphics.Batch()

# Blob handle
blobs = []
blobnumber = 3
blobBatch = pyglet.graphics.Batch()

# Other
pressing_keys=[]


def spawn(dt):
    global number
    for i in range(number):
        cowboy = Cowboy(cowboyBatch, "Cowboy2.png")
        cowboys.append(cowboy)
    number += 1

    for i in range(blobnumber):
        blob = Blob(blobBatch, "blob.png")
        blobs.append(blob)


def moveCharacter(dt):
    if pyglet.window.key.LEFT in pressing_keys:
        player.move(-character_speed, 0)
    if pyglet.window.key.RIGHT in pressing_keys:
        player.move(character_speed, 0)
    if pyglet.window.key.UP in pressing_keys:
        player.move(0, character_speed)
    if pyglet.window.key.DOWN in pressing_keys:
        player.move(0, -character_speed)


@window.event
def on_draw():
    window.clear()
    background_sprite.draw()
    player.sprite.draw()
    for cowboy in cowboys:
        cowboy.draw()
    for blob in blobs:
        blob.draw()
    timer.label.draw()


@window.event
def on_mouse_press(x, y, button, modifier):
    for cowboy in cowboys:
        if button == mouse.LEFT:
            if hit_cowboy(x, y, cowboy.cowboy_sprite.x, cowboy.cowboy_sprite.y) is True:
                cowboys.remove(cowboy)
                break

    for blob in blobs:
        if button == mouse.LEFT:
            if hit_blob(x, y, blob.blob_sprite.x, blob.blob_sprite.y) is True:
                blobs.remove(blob)
                break


@window.event
def on_key_press(symbol, modifiers):
    pressing_keys.append(symbol)


@window.event
def on_key_release(symbol, modifiers):
    pressing_keys.remove(symbol)


def update(dt):
    player.update(dt)
    pos = player.update(dt)
    for cowboy in cowboys:
        if hit_cowboy(player.sprite.x, player.sprite.y, cowboy.cowboy_sprite.x, cowboy.cowboy_sprite.y) is True:
            endGame()
        else:
            cowboy.update(dt, pos)

    for blob in blobs:
        if hit_blob(player.sprite.x, player.sprite.y, blob.blob_sprite.x, blob.blob_sprite.y) is True:
            endGame()
        else:
            blob.update(dt, pos)

    on_draw()

def endGame():
    pyglet.clock.unschedule(update)
    pyglet.clock.unschedule(spawn)
    pyglet.clock.unschedule(moveCharacter)
    pyglet.clock.unschedule(timer.update)
    cowboys.clear()
    blobs.clear()


if __name__ == "__main__":
    timer = Timer()
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.clock.schedule_interval(spawn, spawn_speed)
    pyglet.clock.schedule_interval(moveCharacter, 1.0/60)
    pyglet.clock.schedule_interval(timer.update, 1.0)
    pyglet.app.run()
