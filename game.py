'''
Module docstring
'''

class Room:
    '''
    Class docstring
    '''
    def __init__(self, name):
        self.name = name
        self.description = None
        self.character = None
        self.item = None
        self.linked_rooms = {}

    def set_description(self, description):
        '''
        Function docstring
        '''
        self.description = description

    def get_details(self):
        '''
        Function docstring
        '''
        print(self.name)
        print("--------------------")
        print(self.description)
        for room in self.linked_rooms:
            print("The " + self.linked_rooms[room].name + " is " + room)

    def set_character(self, character):
        '''
        Function docstring
        '''
        self.character = character

    def get_character(self):
        '''
        Function docstring
        '''
        return self.character

    def set_item(self, item):
        '''
        Function docstring
        '''
        self.item = item

    def get_item(self):
        '''
        Function docstring
        '''
        return self.item

    def link_room(self, other, direction):
        '''
        Function docstring
        '''
        self.linked_rooms[direction] = other

    def move(self, direction):
        '''
        Function docstring
        '''
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        print("You can't move there!")
        return self

class Item:
    '''
    Class docstring
    '''
    def __init__(self, name):
        self.name = name
        self.description = None

    def get_name(self):
        '''
        Function docstring
        '''
        return self.name

    def set_description(self, description):
        '''
        Function docstring
        '''
        self.description = description

    def describe(self):
        '''
        Function docstring
        '''
        print("The [" + self.name + "] is here - " + self.description)

class Character:
    '''
    Class docstring
    '''
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.fraze = None
        self.defeated = 0

    def describe(self):
        '''
        Function docstring
        '''
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, fraze):
        '''
        Function docstring
        '''
        self.fraze = fraze

    def talk(self):
        '''
        Function docstring
        '''
        print("[" + self.name + " says]: " + self.fraze)

class Enemy(Character):
    '''
    Class docstring
    '''
    def __init__(self, name, species):
        super().__init__(name, species)
        self.item = None

    def set_weakness(self, item):
        '''
        Function docstring
        '''
        self.item = item

    def fight(self, item):
        '''
        Function docstring
        '''
        return item == self.item

    def get_defeated(self):
        '''
        Function docstring
        '''
        self.defeated = self.defeated + 1
        return self.defeated
