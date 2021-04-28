import pyglet


class Timer:
    def __init__(self):
        self.label = pyglet.text.Label('00:00', font_size=30,
                                       x=1130,
                                       y=870,
                                       anchor_x='center', anchor_y='center')
        self.reset()
    def reset(self):
        self.time = 0
        # self.running = False
        self.label.text = '00:00'
        self.label.color = (255, 255, 255, 255)
    def update(self, dt):
        # if self.running:
            self.time += dt
            m, s = divmod(self.time, 60)
            self.label.text = '%02d:%02d' % (m, s)
            if m >= 5:
                self.label.color = (180, 0, 0, 255)
