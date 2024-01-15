
class Unit:
    def __init__(self, name, att, deff, speed, health, mindam, maxdam):
        self.name = name
        self.att = att
        self.deff = deff
        self.speed=speed
        self.health=health
        self.mindam=mindam
        self.maxdam=maxdam

class Hero:
    def __init__(self, lvl):
        self.lvl = lvl

class endUnit(Unit, Hero):
    pass

