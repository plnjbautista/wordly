# app.py
from flask import Flask, request, jsonify, render_template, session
import os
import secrets
from countries_data import CountriesDataManager
from nlp_processor import TextProcessor, CountryClassifier
from game_logic import CountryNameGame

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Create a game instance to be shared across requests
game_instances = {}

@app.route('/')
def index():
    # Generate a unique session ID if not already present
    if 'session_id' not in session:
        session['session_id'] = secrets.token_hex(16)
    
    return render_template('index.html')

@app.route('/api/start_game', methods=['POST'])
def start_game():
    session_id = session.get('session_id')
    if not session_id:
        return jsonify({'status': 'error', 'message': 'No session found'}), 400
    
    # Create a new game instance for this session
    game_instances[session_id] = CountryNameGame()
    result = game_instances[session_id].start_game()
    
    return jsonify(result)

@app.route('/api/submit_country', methods=['POST'])
def submit_country():
    session_id = session.get('session_id')
    if not session_id or session_id not in game_instances:
        return jsonify({'status': 'error', 'message': 'No active game found'}), 400
    
    data = request.get_json()
    country_name = data.get('country', '')
    
    if not country_name:
        return jsonify({'status': 'error', 'message': 'No country name provided'}), 400
    
    result = game_instances[session_id].process_player_turn(country_name)
    return jsonify(result)

@app.route('/api/game_state', methods=['GET'])
def game_state():
    session_id = session.get('session_id')
    if not session_id or session_id not in game_instances:
        return jsonify({'status': 'inactive', 'message': 'No active game found'})
    
    state = game_instances[session_id].get_game_state()
    return jsonify(state)

if __name__ == '__main__':
    app.run(debug=True)