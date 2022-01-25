from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for the entire game.
        user_choice (str): is the user input.
        play(Card): an instance for Card.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 0
        self.user_choice=''
        self.play = Card()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            new_card = self.play.shuffle_first_card()
            print(f'The card is: {new_card}')
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user for input.

        Args:
            self (Director): An instance of Director.
        """
        
        self.user_choice=input('Higher or lower? (H/L): ')
        

       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        
        second_value=self.play.shuffle_sec_card()
        print(f'Next card was: {second_value}')
        self.score=self.play.compute_score(self.user_choice.capitalize())

    def do_outputs(self):
        """Displays the score. Also asks the player if they want to Play again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        if self.score<=0:
            print('Game Over your score is: 0')
            self.is_playing = False
            return
            
        print(f'Your score is: {self.score}')
        
        play_card = input("Play again? [y/n] ")
        if play_card.lower()=='n':
            print('Thanks for playing with us.')
        self.is_playing = (play_card.lower() == "y")