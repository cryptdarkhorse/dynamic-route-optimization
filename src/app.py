from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from data_fetcher import get_traffic_data, get_weather_data
from route_optimizer import optimize_route
from emissions_calculator import calculate_emissions

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/optimize_route', methods=['POST'])
def optimize_route_endpoint():
    origin = request.form['origin']
    destination = request.form['destination']
    vehicle_type = request.form['vehicle_type']

    # Fetch real-time data
    traffic_data = get_traffic_data(origin, destination)
    weather_data = get_weather_data(origin, destination)

    # Optimize the route
    route_info = optimize_route(origin, destination, traffic_data, weather_data)

    # Calculate emissions
    emissions = calculate_emissions(route_info['distance'], vehicle_type)

    return jsonify({
        'route_info': route_info,
        'emissions': emissions
    })

if __name__ == '__main__':
    app.run(debug=True)

