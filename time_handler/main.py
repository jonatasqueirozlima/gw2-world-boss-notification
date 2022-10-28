from datetime import datetime, timedelta


def convert_to_time(value):
    return value.strftime("%H:%M")    


def convert_to_datetime(value):
    return datetime.strptime(value, '%H:%M')    


def get_time():
    current_time = datetime.now()
    return convert_to_time(current_time)    


def addition_n_minutes(value, minutes):  
    time_converted =  convert_to_datetime(value)

    time_added = time_converted + timedelta(minutes=minutes)

    return convert_to_time(time_added)    
