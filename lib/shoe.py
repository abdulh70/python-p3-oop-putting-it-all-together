#!/usr/bin/env python3
# lib/shoe.py

class Shoe:
    def __init__(self, brand, size, color="Unknown"):
        self.brand = brand
        self.size = size
        self.color = color
        self.condition = "New"

    def cobble(self):
        # Update the message to match what the test expects
        print("Your shoe is as good as new!")
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")