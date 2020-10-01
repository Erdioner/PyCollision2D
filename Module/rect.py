from vector import Vector

class Rect:
    def __init__(self, pos, size, vel=None):
        if isinstance(pos, tuple) or isinstance(pos, list):
            if len(pos) >= 2:
                pos = Vector(pos[0], pos[1])
            else:
                raise ValueError(f"tuple or list must have length >= 2: {len(pos)}")
        if isinstance(size, tuple) or isinstance(size, list):
            if len(size) >= 2:
                size = Vector(size[0], size[1])
            else:
                raise ValueError(f"tuple or list must have length >= 2: {len(size)}")

        if not isinstance(pos, Vector):
            raise TypeError(f"unsupported type(s) for Rect.pos: '{type(pos)}'")
        if not isinstance(size, Vector):
            raise TypeError(f"unsupported type(s) for Rect.size: '{type(size)}'")
        if not isinstance(vel, Vector) and vel != None:
            raise TypeError(f"unsupported type(s) for Rect.vel: '{type(vel)}'")

        self._pos = pos
        self._size = size
        self._vel = vel

    def _get_pos(self):
        return self._pos
    def _get_size(self):
        return self._size
    def _get_vel(self):
        return self._vel

    def _set_pos(self, pos):
        if not isinstance(pos, Vector):
            raise TypeError(f"unsupported type(s) for Rect.pos: '{type(pos)}'")
        self._pos = pos
    def _set_size(self, size):
        if not isinstance(size, Vector):
            raise TypeError(f"unsupported type(s) for Rect.size: '{type(size)}'")
        self._size = size
    def _set_vel(self, vel):
        if not isinstance(vel, Vector) and vel != None:
            raise TypeError(f"unsupported type(s) for Rect.vel: '{type(vel)}'")
        self._vel = vel

    pos = property(_get_pos, _set_pos)
    size = property(_get_size, _set_size)
    vel = property(_get_vel, _set_vel)

    def collides_with_point(self, point):
        if isinstance(point, tuple) or isinstance(point, list):
            if len(point) >= 2:
                point = Vector(point[0], point[1])
            else:
                raise ValueError(f"tuple or list must have length >= 2: {len(point)}")
        if not isinstance(point, Vector):
            raise TypeError(f"unsupported type(s) for Rect.collides_with_point(point): '{type(point)}'")

        inside_x = point.x >= self.pos.x and point.x < self.pos.x+self.size.x
        inside_y = point.y >= self.pos.y and point.y < self.pos.y+self.size.y
        return (inside_x and inside_y)

    def collides_with_rect(self, rect):
        if isinstance(rect, tuple) or isinstance(rect, list):
            if len(rect) >= 4:
                rect = Rect(rect[0:2], rect[2:4])
            else:
                raise ValueError(f"tuple or list must have length >= 4: {len(rect)}")
        if not isinstance(rect, Rect):
            raise TypeError(f"unsupported type(s) for Rect.collides_with_rect(rect): '{type(rect)}'")

        self_left_inside_rect_right = self.pos.x < rect.pos.x + rect.size.x
        self_right_inside_rect_left = self.pos.x + self.size.x > rect.pos.x
        self_top_inside_rect_bottom = self.pos.y < rect.pos.y + rect.size.y
        self_bottom_inside_rect_top = self.pos.y + self.size.y > rect.pos.y
        return (self_left_inside_rect_right and self_right_inside_rect_left and
                self_top_inside_rect_bottom and self_bottom_inside_rect_top)
