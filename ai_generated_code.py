# ChatGPT generated wind chill function
def compute_wind_chill(temperature, wind_speed):
    """
    Compute the wind chill index using the temperature (in Celsius) and wind speed (in km/h).
    Formula used here is the JAG/TI method.
    """
    if temperature < 10 and wind_speed > 4.8:
        wind_chill = 13.12 + 0.6215 * temperature - 11.37 * wind_speed**0.16 + 0.3965 * temperature * wind_speed**0.16
        return wind_chill
    else:
        return temperature

# Example usage
temperature = float(input("Enter the temperature in Celsius: "))
wind_speed = float(input("Enter the wind speed in km/h: "))
wind_chill = compute_wind_chill(temperature, wind_speed)
print(f"The wind chill index is {wind_chill:.2f} Celsius")




