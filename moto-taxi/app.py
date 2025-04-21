"""
Main application module for Moto-Taxi service
"""
from flask import Flask, jsonify, request, send_from_directory, send_file, abort
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Simulated database (in a real app, this would be a proper database)
users = []
drivers = []
rides = []

@app.route('/')
def serve_frontend():
    """Serve the main frontend page"""
    try:
        return send_file('index.html')
    except FileNotFoundError:
        abort(404)

@app.route('/favicon.ico')
def favicon():
    """Serve the favicon"""
    return '', 204  # Return empty response for now

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files"""
    try:
        return send_file(filename)
    except FileNotFoundError:
        abort(404)

@app.route('/api/register', methods=['POST'])
def register_user():
    """Register a new user"""
    data = request.get_json()
    required_fields = ['name', 'email', 'phone', 'password']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios faltando'}), 400
    
    # Check if email already exists
    if any(user['email'] == data['email'] for user in users):
        return jsonify({'error': 'Email já cadastrado'}), 400
    
    user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email'],
        'phone': data['phone'],
        'password': data['password'],  # In a real app, this would be hashed
        'created_at': datetime.now().isoformat()
    }
    
    users.append(user)
    return jsonify({'message': 'Usuário cadastrado com sucesso'})

@app.route('/api/login', methods=['POST'])
def login():
    """Handle user login"""
    data = request.get_json()
    
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email e senha são obrigatórios'}), 400
    
    # Find user by email and password
    user = next((user for user in users 
                 if user['email'] == data['email'] and 
                 user['password'] == data['password']), None)
    
    if not user:
        return jsonify({'error': 'Email ou senha inválidos'}), 401
    
    # In a real app, you would generate and return a JWT token here
    return jsonify({'message': 'Login realizado com sucesso'})

@app.route('/api/request-ride', methods=['POST'])
def request_ride():
    """Handle ride requests"""
    data = request.get_json()
    
    if not data or 'pickup' not in data or 'destination' not in data:
        return jsonify({'error': 'Campos obrigatórios faltando'}), 400
    
    ride = {
        'id': len(rides) + 1,
        'status': 'searching',
        'pickup': data['pickup'],
        'destination': data['destination'],
        'estimated_price': data.get('estimated_price', 0),
        'created_at': datetime.now().isoformat(),
        'driver_id': None,
        'user_id': None  # In a real app, this would come from the authenticated user
    }
    
    rides.append(ride)
    return jsonify(ride)

@app.route('/api/driver/register', methods=['POST'])
def register_driver():
    """Register a new driver"""
    data = request.get_json()
    required_fields = ['name', 'email', 'phone', 'license_number', 'vehicle_info']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios faltando'}), 400
    
    # Check if email or license number already exists
    if any(driver['email'] == data['email'] for driver in drivers):
        return jsonify({'error': 'Email já cadastrado'}), 400
    
    if any(driver['license_number'] == data['license_number'] for driver in drivers):
        return jsonify({'error': 'CNH já cadastrada'}), 400
    
    driver = {
        'id': len(drivers) + 1,
        'status': 'offline',
        'rating': 5.0,
        'total_rides': 0,
        'created_at': datetime.now().isoformat(),
        **data
    }
    
    drivers.append(driver)
    return jsonify({'message': 'Motorista cadastrado com sucesso'})

@app.route('/api/driver/status', methods=['POST'])
def update_driver_status():
    """Update driver's availability status"""
    data = request.get_json()
    
    if not data or 'driver_id' not in data or 'status' not in data:
        return jsonify({'error': 'Campos obrigatórios faltando'}), 400
    
    driver = next((driver for driver in drivers if driver['id'] == data['driver_id']), None)
    
    if not driver:
        return jsonify({'error': 'Motorista não encontrado'}), 404
    
    if data['status'] not in ['online', 'offline', 'busy']:
        return jsonify({'error': 'Status inválido'}), 400
    
    driver['status'] = data['status']
    return jsonify({'message': 'Status atualizado com sucesso'})

@app.route('/api/ride/<int:ride_id>/status', methods=['GET'])
def get_ride_status(ride_id):
    """Get the current status of a ride"""
    ride = next((ride for ride in rides if ride['id'] == ride_id), None)
    
    if not ride:
        return jsonify({'error': 'Corrida não encontrada'}), 404
    
    return jsonify(ride)

@app.route('/api/ride/<int:ride_id>/cancel', methods=['POST'])
def cancel_ride(ride_id):
    """Cancel a ride"""
    ride = next((ride for ride in rides if ride['id'] == ride_id), None)
    
    if not ride:
        return jsonify({'error': 'Corrida não encontrada'}), 404
    
    if ride['status'] not in ['searching', 'accepted']:
        return jsonify({'error': 'Não é possível cancelar esta corrida'}), 400
    
    ride['status'] = 'cancelled'
    return jsonify({'message': 'Corrida cancelada com sucesso'})

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Recurso não encontrado'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    app.run(port=8000, debug=True)
