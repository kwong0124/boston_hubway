from datetime import datetime
from typing import List

from sqlalchemy import create_engine, text

db_path = "sqlite:////Users/kathrynklarich1/Documents/SideProjects/boston_hubway/hubway.db"
engine = create_engine(db_path)

# 0|id|INTEGER|0||0
# 1|station|TEXT|0||0
# 2|municipality|TEXT|0||0
# 3|lat||0||0
# 4|lng||0||0

# TODO: do this with slots
class Station(object):
    def __init__(self, name: str, id: int, municipality: str, lat: float, lon: float):
        self.name = name
        self.id = id
        self.municipality = municipality
        self.lat = lat
        self.lon = lon

# 0|id|INTEGER|0||0
# 1|duration|INTEGER|0||0
# 2|start_date|DATETIME|0||0
# 3|start_station|INTEGER|0||0
# 4|end_date|DATETIME|0||0
# 5|end_station|INTEGER|0||0
# 6|bike_number|TEXT|0||0
# 7|sub_type|TEXT|0||0
# 8|zip_code|TEXT|0||0
# 9|birth_date|REAL|0||0
# 10|gender|TEXT|0||0

class Trip(object):
    def __init__(self, duration: int, start_date: datetime, start_station: int, end_date: datetime, end_station: int,
                 bike_number: str, sub_type: str, zip_code: str, birth_date, gender: str):
        self.duration = duration
        self.start_date = start_date
        self.end_date = end_date
        self.bike_number = bike_number
        self.sub_type: sub_type
        self.zip_code = zip_code
        self.birth_date: birth_date
        self.gender = gender
        self.start_station = start_station
        self.end_station = end_station

def get_stations()->List[Station]:
    connection = engine.connect()
    stations = []
    try:
        result = connection.execute(text("select * from stations"))
        for r in result:
            station = Station(name=r.station, id=r.id, municipality=r.municipality, lat=r.lat, lon=r.lng)
            stations.append(station)
    except Exception as e:
        raise e
    finally:
        connection.close()
    return stations

def get_trips() -> List[Trip]:
    connection = engine.connect()
    trips = []
    try:
        result = connection.execute(text("select * from trips limit 1000"))
        for r in result:
            trip = Trip(duration = r.duration, start_date=r.start_date, start_station=r.start_station,
                        end_date=r.end_date, end_station=r.end_station, bike_number=r.bike_number, sub_type=r.sub_type,
                        zip_code=r.zip_code, birth_date=r.birth_date, gender=r.gender)
            trips.append(trip)
    except Exception as e:
        raise e
    finally:
        connection.close()
    return trips

if __name__ == "__main__":
    # stations = get_stations()
    # for r in stations:
    #     print(r)
    # stations = get_stations()
    # for s in stations:
    #     print(f"{s.name}: {s.id}, {s.municipality}")
    trips = get_trips()
    for t in trips:
        print(f"start: {t.start_station} {t.start_date} end: {t.end_station} {t.end_date} duration: {t.duration}seconds")
