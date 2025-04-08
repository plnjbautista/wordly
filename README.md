# Documentation

## Overview and Introduction

### App Name
Worldly Words

### Purpose
The Worldly Words is an interactive NLP-powered application where users take turns with the system to name countries that start with a randomly selected letter. The system utilizes Natural Language Processing techniques to validate inputs, manage game logic, and simulate an intelligent opponent.

The application demonstrates essential NLP components:
- Text preprocessing (normalization, cleaning, tokenization)
- Feature extraction (TF-IDF vectorization)
- Model training (Naive Bayes classification)
- Model evaluation (accuracy metrics)

### Technology Stack

#### Backend
- **Flask**: v2.3.3 - Web framework for the API
- **Python**: v3.9+ - Programming language
- **scikit-learn**: v1.3.0 - Machine learning library for NLP model
- **NLTK**: v3.8.1 - Natural Language Toolkit for text processing
- **NumPy**: v1.24.3 - Numerical computations
- **Pandas**: v2.0.3 - Data manipulation

#### Frontend
- **HTML5** - Structure
- **CSS3** - Styling
- **JavaScript** - Client-side logic

## Functional Requirements

### Core Features

#### 1. Text Preprocessing
The system implements several text preprocessing techniques crucial for NLP:
- **Case normalization**: Converts all text to lowercase for consistent processing
- **Special character removal**: Eliminates punctuation and other non-alphabetical characters
- **Tokenization**: Breaks text into individual words or tokens
- **Country name normalization**: Handles prefixes like "The" or "Republic of" for better matching

#### 2. Feature Extraction
- **TF-IDF Vectorization**: Converts text into numerical features
- **N-gram processing**: Captures sequences of words (useful for multi-word country names)

#### 3. Naive Bayes Classification
- **Custom-trained model**: Identifies whether user input is a valid country name
- **Training dataset**: Includes all world countries as positive examples and non-countries as negative examples
- **Confidence scoring**: Provides probability estimates for classifications

#### 4. Game Logic
- **Turn-based system**: Alternates between user and computer
- **Input validation**: Verifies country names using the trained model
- **History tracking**: Prevents repetition of previously mentioned countries
- **Response generation**: Creates varied system responses

### Libraries and Packages
- **flask**: Web server framework
- **flask-cors**: Cross-origin resource sharing support
- **scikit-learn**: ML algorithms including Naive Bayes and TF-IDF vectorizer
- **nltk**: Text preprocessing tools
- **pandas**: Dataset manipulation
- **numpy**: Numerical operations

# Code Structure

## File Names and Descriptions

### `countries_data.py`
- **Purpose**: Manages the database of countries.
  - Contains the list of countries used in the game.
  - Handles the generation of positive and negative samples for training the model.

### `model_trainer.py`
- **Purpose**: Trains and saves the NLP model for country name classification.
  - Handles the training of the Naive Bayes classifier using the training data.
  - Saves the trained model for later use.

### `nlp_processor.py`
- **Purpose**: Contains NLP components for text preprocessing and loading the trained classifier.
  - Implements text normalization, tokenization, and TF-IDF feature extraction.
  - Loads the pre-trained NLP model and uses it for classification.

### `game_logic.py`
- **Purpose**: Implements the core game logic and rules.
  - Handles user turns, validates the country name using the model, and tracks previously mentioned countries.
  - Generates responses and manages the flow of the game.

### `app.py`
- **Purpose**: Main application file for the Flask server.
  - Defines the Flask routes and API endpoints for interacting with the frontend.
  - Manages the game session, user input, and system output.

### `index.html`
- **Purpose**: Contains the structure of the game interface.
  - **HTML**: Provides the skeleton of the webpage with input fields and areas to display the game status and responses.
  - **CSS**: Styles the layout, including buttons, input fields, and game progress displays.
  - **JavaScript**: Implements client-side logic, sending user input to the Flask API and displaying the system’s response dynamically.


## Future Enhancements and Roadmap

### Known Limitations
1. **Limited dataset**: The system only recognizes officially recognized countries
2. **Single language support**: Currently only handles English country names
3. **Basic frontend**: Minimal user interface without advanced features
4. **Limited response variety**: System responses follow simple templates

### Planned Features and Improvements
1. **Difficulty levels**: Add easy/medium/hard modes with different letter sets
2. **Multilingual support**: Add country names in different languages
3. **Enhanced NLP model**: Implement more advanced classification techniques
4. **User accounts**: Track individual player statistics and high scores
5. **More varied responses**: Implement a more sophisticated language generation model
6. **Additional game modes**: Variants like cities, famous landmarks, or other geographic features