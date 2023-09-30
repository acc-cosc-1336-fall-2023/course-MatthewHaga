def get_hour (epach_seconds):
    hours = epach_seconds // 3600 % 24
    return hours

def get_minutes(epach_seconds): 
    minutes = (epach_seconds // 60) % 60 
    return minutes 

def get_seconds(epach_seconds): 
    seconds = (epach_seconds % 3600) % 60
    return seconds 

def get_time (epach_seconds):
    h = str (get_hour(epach_seconds)) .zfill(2)
    m = str (get_minutes(epach_seconds)).zfill(2)
    s = str (get_seconds(epach_seconds)).zfill(2)

    print(f'{h}:{m}:{s}')