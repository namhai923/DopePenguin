import pyglet


def hit_cowboy(x, y, position_x, position_y):
    target_width = 45/2
    target_height = 45/2
    if range_x(position_x, target_width, x) is True and range_y(position_y, target_height, y) is True:
        return True
    return False


def hit_blob(x, y, position_x, position_y):
    target_width = 40
    target_height = 40
    if range_x(position_x, target_width, x) is True and range_y(position_y, target_height, y) is True:
        return True
    return False


def range_x(position_x, width, x):
    return position_x - width <= x <= position_x + width


def range_y(position_y, height, y):
    return position_y - height <= y <= position_y + height
