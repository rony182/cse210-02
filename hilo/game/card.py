import random

# begin class declaration for stack of 13 cards
"""A stack of cards numbered 1 - 13 is used.

    the responsibility of the Card class is to keep track of the 
    number on the card displayed.

    Attributes:
        value (int): the number on the card displayed
        points (int): the number of points the card is worth.       
"""
class Card:
    """ Constructs an instance for the displayed Card with a
    value and points
    
        args:
            self (Card): An instand of the Card
            """
    def __init__(self):
        self.f_value = 0
        self.s_value = 0
        self.points = 300
        self.hilo = ""
    
    """Generates a randon interger between 1 - 13 representing 
    the flip of the card
    
        args:
            self (Card): An instance of Card
        """
    def display_card(self):
        self.f_value = random.randint(1, 13)
        self.s_value = random.randint(1, 13)
        self.points = 100 if self.s_value > self.f_value and self.hilo == "h" else -75 if self.s_value > self.f_value and self.hilo == "l" else 100 if self.s_value < self.f_value and self.hilo == "l" else -75 if self.s_value < self.f_value and self.hilo == "h" else 0
