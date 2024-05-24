
def get_coordinate(record):
    treasure, cordinate = record
    return cordinate

def convert_coordinate(coordinate):
    return coordinate[0], coordinate[1]

def create_record(azara_record, rui_record):
     tesoro, coordenada = azara_record 
     ubicación, coordenada, cuadrante= rui_record
     if azara_record == rui_record:
        return azara_record + rui_record
     else: 
         return "no coincide"
