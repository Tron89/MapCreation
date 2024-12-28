import random

class WFCCell:
    def __init__(self, row, col, posibilities):
        self.row = row
        self.column = col

        self.posibilities = posibilities
        self.entropy = len(posibilities)
        self.collapsed = False

    def collapse(self):
        if len(self.posibilities) == 0:
            raise Exception("The values you just put are invalid (or else contact to the creator, he don't know what is doing)")
        self.posibilities = [random.choice(self.posibilities)]
        self.entropy = 1
        self.collapsed = True
