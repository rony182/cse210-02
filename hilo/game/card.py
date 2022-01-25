import random

# begin class declaration for stack of 13 cards
"""A stack of cards numbered 1 - 13 is used.

    the responsibility of the Card class is to keep track of the 
    number on the card displayed.

    Attributes:
        f_value (int): the number of the first card.
        s_value (int): the number of the second card.
        points (int): Start at 300. The number of points accumulated by the player. 
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
        
    
    
    def shuffle_first_card(self):
        """Generates a randon interger between 1 - 13 representing 
    the flip of the first card
    
        args:
            self (Card): An instance of Card
        """
        self.f_value = random.randint(1, 13)
        return self.f_value
        
        
    def shuffle_sec_card(self):
        """Generates a randon interger between 1 - 13 representing 
    the flip of the second card
    
        args:
            self (Card): An instance of Card
        """
        self.s_value = random.randint(1, 13)
        while self.s_value==self.f_value:
            self.s_value = random.randint(1, 13)
        return self.s_value
        
    def compute_score(self, player_answer):
        """Computes the score comparing the two values and the user input.
    
        args:
            self (Card): An instance of Card
        """
        
        if (self.f_value<self.s_value and player_answer=='H') or (self.s_value<self.f_value and player_answer=='L'):
            self.points+=100
        else:
            self.points-=75
            
        return self.points
        