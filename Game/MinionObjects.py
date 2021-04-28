import resources
import pyglet
from random import randint


class Cowboy:
    def __init__(self, batch, image):
        self.posx = randint(0, 1200)
        self.posy = randint(450, 950)
        self.velx = 0
        self.vely = 0
        if image is not None:
            cowboy = pyglet.resource.image(image)
            cowboy_seq = pyglet.image.ImageGrid(cowboy, 4 ,8 ,item_width = 45, item_height = 45)
            cowboy_animation = pyglet.image.Animation.from_image_sequence(cowboy_seq[10:20], 0.1, loop=True)
            self.cowboy_sprite = pyglet.sprite.Sprite(cowboy_animation, x=self.posx, y=self.posy, batch=batch)

            self.cowboy_sprite.image.anchor_x = 45 / 2
            self.cowboy_sprite.image.anchor_y = 45 / 2
            self.cowboy_sprite.rotation = 0


    def draw(self):
        self.cowboy_sprite.draw()


    def update(self, dt, pos):
        if self.cowboy_sprite.x <= pos[0] and self.cowboy_sprite.y < pos[1]:
            self.cowboy_sprite.x += 50*dt
            self.cowboy_sprite.y += 50*dt
        elif self.cowboy_sprite.x <= pos[0] and self.cowboy_sprite.y > pos[1]:
            self.cowboy_sprite.x += 50*dt
            self.cowboy_sprite.y -= 50*dt
        elif self.cowboy_sprite.x >= pos[0] and self.cowboy_sprite.y > pos[1]:
            self.cowboy_sprite.x -= 50*dt
            self.cowboy_sprite.y -= 50*dt
        else:
            self.cowboy_sprite.x -= 50*dt
            self.cowboy_sprite.y += 50*dt


class Blob:
    def __init__(self, batch, image):
        self.posx = randint(0, 1200)
        self.posy = randint(450, 950)
        self.velx = 0
        self.vely = 0
        if image is not None:
            blob = pyglet.resource.image(image)
            blob_seq = pyglet.image.ImageGrid(blob, 1 ,8 ,item_width = 80, item_height = 80)
            blob_animation = pyglet.image.Animation.from_image_sequence(blob_seq[0:7], 0.1, loop=True)
            self.blob_sprite = pyglet.sprite.Sprite(blob_animation, x=self.posx, y=self.posy, batch=batch)

            self.blob_sprite.image.anchor_x = 80 / 2
            self.blob_sprite.image.anchor_y = 80 / 2
            self.blob_sprite.rotation = 0


    def draw(self):
        self.blob_sprite.draw()


    def update(self, dt, pos):
        if self.blob_sprite.x <= pos[0] and self.blob_sprite.y < pos[1]:
            self.blob_sprite.x += 100*dt
            self.blob_sprite.y += 100*dt
        elif self.blob_sprite.x <= pos[0] and self.blob_sprite.y > pos[1]:
            self.blob_sprite.x += 100*dt
            self.blob_sprite.y -= 100*dt
        elif self.blob_sprite.x >= pos[0] and self.blob_sprite.y > pos[1]:
            self.blob_sprite.x -= 100*dt
            self.blob_sprite.y -= 100*dt
        else:
            self.blob_sprite.x -= 100*dt
            self.blob_sprite.y += 100*dt
