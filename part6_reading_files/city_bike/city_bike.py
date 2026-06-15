import math

def get_station_data(filename: str):
    dict_of_stations = {}
    saving_eveything = []
    index_latitude = 0
    index_longitude = 0
    index_id = 0
    index_name = 0
    with open (filename) as new_file:
        for i in new_file:
            parts = i.strip().split(";")
            if parts[0] == "Longitude":
                if "Latitude" in parts:
                    index_latitude = parts.index("Latitude")
                if "Longitude" in parts:
                    index_longitude = parts.index("Longitude")
                if "id" in parts:
                    index_id = parts.index("id")
                if "name" in parts:
                    index_name = parts.index("name")
                continue
            dict_of_stations[parts[index_name]] = float(parts[index_longitude]),float(parts[index_latitude])
                
    return dict_of_stations


def distance(stations: dict, station1: str, station2: str):
    longitude1,latitude1 = stations[station1]
    longitude2,latitude2 = stations[station2]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    max_distance = 0
    greatest_station1 = ""
    greatest_station2 = ""

    for station1 in stations:
        for station2 in stations:

            d = distance(stations, station1, station2)

            if d > max_distance:
                max_distance = d
                greatest_station1 = station1
                greatest_station2 = station2

    return greatest_station1, greatest_station2, max_distance





stations = get_station_data("stations1.csv")
print(distance(stations, "Kaivopuisto", "Laivasillankatu"))
station1,station2,max_distance = greatest_distance(stations)
print(station1,station2,max_distance)