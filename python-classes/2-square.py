#!/usr/bin/python3
'''a class called square is initialized'''


class square:
    '''a private instance is made to an attribute with the name size'''
    def __init__(self, size=0):
        self.size = size
        '''raise an error if the data type is incorrect'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
         '''raise an error if the data is less that 0'''
        if size < 0:
            raise ValueError("size must be >= 0")
