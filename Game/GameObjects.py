import resources
import pyglet
from random import randint

class PlayerObject:
    pos = []
    def __init__(self, posx, posy, image=None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        if image is not None:
            image = pyglet.resource.image(image)
            self.sprite = pyglet.sprite.Sprite(image, x=self.posx, y=self.posy)


    def draw(self):
        self.sprite.draw()


    def update(self, dt):
        pos=[0,0]
        pos[0] = self.sprite.x
        pos[1] = self.sprite.y
        return pos


    def move(self, x, y):
        if ((self.sprite.x <= 0.0 - 12 and x < 0) or (self.sprite.x >= 1200 - 45 and x > 0) or (self.sprite.y <= 0 and y < 0) or (self.sprite.y >= 900-35 and y > 0)):
            return
        self.sprite.x += x
        self.sprite.y += y
