import json

class Doctor:
    def __init__(self, lat, lon, name, hospital):
        self.lat=lat
        self.lon=lon
        self.name=name
        self.hospital=hospital

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)