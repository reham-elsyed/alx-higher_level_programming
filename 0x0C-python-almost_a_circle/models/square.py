#!/usr/bin/python3
"""Define class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Class square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[square] (self.id) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            for arg in args:
                    setattr(self, arg[0], arg[1])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
