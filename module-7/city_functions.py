# Frederick Costello
# M7 Assignment CSD-325
# 05/03/2026

# "TEST CASES"

# Resources Microsoft copilot, google.
# Function created that returns a string of city, country.
# Parameter addded that calls for population.
# Parameter added that makes for population optional.
# Paramater added that calls for language to be added.
# Paramater added that calls for languages to be optional
# Final Paramater added that calls for 1st string: City, Country. 2nd string: City, Country, Population. and 3rd string: City, Country, Population & Language.
# Final test results were successful

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