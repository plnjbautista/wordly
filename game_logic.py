# game_logic.py
import random
from countries_data import CountriesDataManager
from nlp_processor import TextProcessor, CountryClassifier

class CountryNameGame:
    """
    A class to manage the logic of a country name game where players and the computer take turns 
    naming countries that start with a specified letter.
    
    The game uses a combination of a country database and a machine learning model to validate if 
    an input is a valid country name and if it starts with the correct letter.
    
    The game involves the following:
    1. A player and the computer take turns naming countries starting with a randomly chosen letter.
    2. The game ensures that each country is used only once and that it matches the starting letter.
    3. The player's input is validated both by a pre-trained model and by a country dataset.
    4. The game ends when the player makes an invalid move, repeats a country, or when the computer runs out of options.
    
    Attributes:
    - data_manager: Instance of CountriesDataManager for managing country data.
    - text_processor: Instance of TextProcessor for text normalization and cleaning.
    - classifier: Instance of CountryClassifier for classifying if an input is a valid country.
    - used_countries: Set of countries already used in the game.
    - current_letter: The current letter that countries must start with.
    - game_active: Boolean flag indicating if the game is ongoing.
    - turns_count: Counter for the number of turns taken in the game.
    
    Methods:
    - is_valid_country(country_name): Validates if a given country name is correct using both the model and dataset.
    - country_starts_with_letter(country_name, letter): Checks if the country starts with the specified letter.
    - start_game(): Starts a new game by selecting a random letter from available options.
    - process_player_turn(country_name): Processes the player's turn, checking for validity, starting letter, and uniqueness.
    - computer_turn(): Processes the computer's turn, selecting a random unused country that starts with the current letter.
    - get_game_state(): Returns the current state of the game, including used countries and the current letter.
    """
    def __init__(self):
        """Initialize the game with countries data and NLP model"""
        # Initialize data managers and processors
        self.data_manager = CountriesDataManager()
        self.text_processor = TextProcessor()
        self.classifier = CountryClassifier()  # Now loads the pre-trained model
        
        # Initialize game state
        self.used_countries = set()
        self.current_letter = None
        self.game_active = False
        self.turns_count = 0
    
    def is_valid_country(self, country_name):
        """Check if input is a valid country using the trained classifier and database"""
        # First, preprocess the input
        processed_input = self.text_processor.preprocess_text(country_name)
        
        # Check with machine learning model
        ml_prediction = self.classifier.is_valid_country(processed_input)
        
        # Check if it's in our database
        in_database = self.data_manager.is_valid_country(processed_input)
        
        # Both conditions must be met
        return ml_prediction and in_database
    
    def country_starts_with_letter(self, country_name, letter):
        """Check if the country starts with the specified letter"""
        processed_input = self.text_processor.preprocess_text(country_name)
        return processed_input.startswith(letter.lower())
    
    def start_game(self):
        """Start a new game by selecting a random letter"""
        # Reset game state
        self.used_countries = set()
        self.turns_count = 0
        
        # Select a letter that has countries
        available_letters = self.data_manager.get_available_starting_letters()
        
        if not available_letters:
            return {"status": "error", "message": "No countries available to play"}
        
        self.current_letter = random.choice(available_letters)
        self.game_active = True
        
        return {
            "status": "success",
            "message": f"Game started! Name a country that starts with '{self.current_letter.upper()}'",
            "letter": self.current_letter.upper()
        }
    
    def process_player_turn(self, country_name):
        """Process the player's turn"""
        if not self.game_active:
            return {"status": "error", "message": "No active game. Start a new game first."}
        
        # Preprocess the input
        processed_input = self.text_processor.preprocess_text(country_name)
        
        # Check if the country is valid
        if not self.is_valid_country(processed_input):
            self.game_active = False
            return {
                "status": "game_over", 
                "message": f"'{country_name}' is not a valid country. Game over!",
                "reason": "invalid_country"
            }
        
        # Check if it starts with the correct letter
        if not self.country_starts_with_letter(processed_input, self.current_letter):
            self.game_active = False
            return {
                "status": "game_over", 
                "message": f"'{country_name}' doesn't start with the letter '{self.current_letter.upper()}'. Game over!",
                "reason": "wrong_letter"
            }
        
        # Check if the country has been used already
        if processed_input in self.used_countries:
            self.game_active = False
            return {
                "status": "game_over", 
                "message": f"'{country_name}' has already been used. Game over!",
                "reason": "already_used"
            }
        
        # If all checks pass, add the country to used countries
        self.used_countries.add(processed_input)
        self.turns_count += 1
        
        # Now it's the computer's turn
        return self.computer_turn()
    
    def computer_turn(self):
        """Computer's turn to select a country"""
        # Get countries that start with the current letter and haven't been used
        available_countries = [
            country for country in self.data_manager.get_countries_by_letter(self.current_letter)
            if country not in self.used_countries
        ]
        
        # If no countries are available, the computer loses
        if not available_countries:
            self.game_active = False
            return {
                "status": "game_over", 
                "message": "I can't think of any more countries with this letter. You win!",
                "reason": "computer_out_of_options"
            }
        
        # Choose a random country from available options
        computer_choice = random.choice(available_countries)
        self.used_countries.add(computer_choice)
        self.turns_count += 1
        
        return {
            "status": "success",
            "message": f"I choose '{computer_choice.title()}'. Your turn!",
            "computer_choice": computer_choice.title(),
            "turn": self.turns_count
        }
    
    def get_game_state(self):
        """Return the current state of the game"""
        if not self.game_active:
            return {"status": "inactive", "message": "No active game"}
        
        return {
            "status": "active",
            "current_letter": self.current_letter.upper(),
            "used_countries": [country.title() for country in self.used_countries],
            "turns_count": self.turns_count
        }