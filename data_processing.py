import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps

def aggregate(aggregation_key, aggregation_function, dict_list):
    temps = []
    for item in dict_list:
        try:
            temps.append(float(item[aggregation_key]))
        except ValueError:
            temps.append(item[aggregation_key])
    return aggregation_function(temps)


# Print the average temperature of all the cities

print("The average temperature of all the cities:")
avg = aggregate('temperature', lambda x: sum(x)/len(x), cities)
print(avg)
print()


# Print all cities in Germany

print("All cities in Germany")
filtered_list = filter(lambda x: x["country"]  == "Germany", cities)
germany = aggregate('city', lambda x: x, filtered_list)
print(germany)
print()

# Print all cities in Spain with a temperature above 12°C

print("All cities in Spain with temperature above 12°C")
spain_only = filter(lambda x: x["country"] == "Spain", cities)
spain_above12 = filter(lambda x: float(x["temperature"]) > 12, spain_only)
city_only = aggregate('city', lambda x: x, spain_above12)
print(city_only)
print()

# Count the number of unique countries

print("Number of unique countires")
all_countries = aggregate('country', lambda x: x, cities)
all_countries = set(all_countries)
print(len(all_countries))
print()

# Print the average temperature for all the cities in Germany

print("Average temperature for all the cities in Germany")
germany_only = filter(lambda x: x['country'] == "Germany", cities)
germany_avg = aggregate('temperature',lambda x: sum(x) / len(x) ,germany_only)
print(germany_avg)
print()

# Print the max temperature for all the cities in Italy

print("Max temperature for all the cities in Italy")
italy_only = filter(lambda x: x['country'] == "Italy", cities)
italy_max = aggregate('temperature', lambda x: max(x), italy_only)
print(italy_max)
print()
