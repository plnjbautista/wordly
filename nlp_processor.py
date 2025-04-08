# nlp_processor.py

import re
import os
import joblib

class TextProcessor:
    """
    A class responsible for preprocessing text input to prepare it for further analysis.
    
    This class provides methods to normalize and clean text data by:
    - Converting text to lowercase.
    - Removing punctuation and extra spaces.
    - Stripping leading and trailing spaces.
    
    Method:
    - preprocess_text(text): Takes a string 'text', normalizes it by removing punctuation, extra spaces, 
      and converting it to lowercase, and then returns the cleaned text.
    """
    def preprocess_text(self, text):
        """Normalize and clean text input"""
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation and extra spaces
        text = re.sub(r'[^\w\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        return text

class CountryClassifier:
    """
    A class to classify if a given input is a valid country name using a pre-trained machine learning model.
    
    The class leverages a text processor to clean the input text and a pre-trained model to make predictions.
    
    Steps:
    1. Initializes the class by loading the trained model from disk.
    2. Uses the loaded model to predict if a given input is a valid country.
    
    The model is expected to be pre-trained and saved as 'country_classifier_model.joblib'. If the model file
    is not found, a FileNotFoundError is raised with a recommendation to train the model first.
    
    Methods:
    - _load_model(): Loads the pre-trained model from disk.
    - is_valid_country(country_name): Preprocesses the input country name, then uses the model to predict if 
      the input is a valid country. Returns a boolean indicating the result of the prediction.
    """
    def __init__(self):
        """Initialize by loading the trained model"""
        self.text_processor = TextProcessor()
        self.model = self._load_model()
    
    def _load_model(self):
        """Load the pre-trained model from disk"""
        model_path = 'country_classifier_model.joblib'
        
        # Check if model exists
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"Model file not found at {model_path}. "
                f"Please run 'model_trainer.py' first to train the model."
            )
        
        print(f"Loading model from {model_path}...")
        return joblib.load(model_path)
    
    def is_valid_country(self, country_name):
        """Check if input is a valid country using the trained classifier"""
        # First, preprocess the input
        processed_input = self.text_processor.preprocess_text(country_name)
        
        # Use the model to predict if it's a country
        prediction = self.model.predict([processed_input])[0]
        
        return bool(prediction)