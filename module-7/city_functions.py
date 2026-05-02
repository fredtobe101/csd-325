# city_functions.py
def city_country(city, country, population=None, language=None):
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    elif language:
        return f"{city}, {country}, {language}"
    else:
        return f"{city}, {country}"


# Calling the function at least three times
print(city_country("Santiago", "Chile"))
print(city_country("Los Angeles", "USA", "population=3,891,400"))
print(city_country("Vancouver", "Canada", "population=776,584", "Canadian French"))