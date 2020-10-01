from vector import Vector
from rect import Rect
import math

class Ray:
    def __init__(self, pos, dir):
        if isinstance(pos, tuple) or isinstance(pos, list):
            if len(pos) >= 2:
                pos = Vector(pos[0], pos[1])
            else:
                raise ValueError(f"tuple or list must have length >= 2: {len(pos)}")
        if isinstance(dir, tuple) or isinstance(dir, list):
            if len(dir) >= 2:
                dir = Vector(dir[0], dir[1])
            else:
                raise ValueError(f"tuple or list must have length >= 2: {len(dir)}")

        if not isinstance(pos, Vector):
            raise TypeError(f"unsupported type(s) for Rect.pos: '{type(pos)}'")
        if not isinstance(dir, Vector):
            raise TypeError(f"unsupported type(s) for Rect.size: '{type(size)}'")

        self._pos = pos
        self._dir = dir

    def _get_pos(self):
        return self._pos
    def _get_dir(self):
        return self._dir

    def _set_pos(self, pos):
        if not isinstance(pos, Vector):
            raise TypeError(f"unsupported type(s) for Rect.pos: '{type(pos)}'")
        self._pos = pos
    def _set_dir(self, dir):
        if not isinstance(dir, Vector):
            raise TypeError(f"unsupported type(s) for Rect.size: '{type(dir)}'")
        self._dir = dir

    pos = property(_get_pos, _set_pos)
    dir = property(_get_dir, _set_dir)

    def collision_point_with_rect(self, rect):
        contact_normal = Vector(0, 0) # Point of contact
        contact_point = Vector(0, 0)  # Normal at point of contact from rectangle

        # Cache division, speed up calculation
        inv_dir = Vector(
            1 / self.dir.x if self.dir.x != 0 else math.inf,
            1 / self.dir.y if self.dir.y != 0 else math.inf
        )

        # Calculate intersection with rectangle bounding axes
        t_near = Vector(
            (rect.pos.x - self.pos.x) * inv_dir.x,
            (rect.pos.y - self.pos.y) * inv_dir.y
        )
        t_far = Vector(
            (rect.pos.x + rect.size.x - self.pos.x) * inv_dir.x,
            (rect.pos.y + rect.size.y - self.pos.y) * inv_dir.y
        )

        # If t_near or t_far is NaN reject
        if t_near.x == math.nan or t_near.y == math.nan:
            return False
        if t_far.x == math.nan or t_far.y == math.nan:
            return False

        # If t_near is further than t_far, swap them
        if t_near.x > t.far.x:
            t_near.x, t_far.x = t_far.x, t_near.x # Swap t_near.x and t_far.x
        if t_near.y > t_far.y:
            t_near.y, t_far.y = t_far.y, t_near.y # Swap t_near.y and t_far.y

        # Early rejection
        if t_near.x > t_far.y or t_near.y > t_far.x:
            return False

        t_hit_near = max(t_near.x, t_near.y) # Closest 'time' will be the first contact
        t_hit_far = min(t_far.x, t_far.y)    # Furthest 'time' is the contact on the opposite side

        # Reject if ray direction is pointing away from object
        if t_hit_near < 0:
            return False

        # Continue: FLAG: Contact point of collision from parametric line equation