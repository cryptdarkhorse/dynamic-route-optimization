# Function to calculate emissions based on route distance and vehicle type
def calculate_emissions(distance, vehicle_type):
    # Placeholder values for emissions based on vehicle type
    emissions_per_km = {
        'gasoline': 0.12,  # kg CO₂/km
        'diesel': 0.15,
        'electric': 0.0
    }

    emissions = distance * emissions_per_km.get(vehicle_type, 0.12)
    return emissions
