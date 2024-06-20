from datetime import datetime, timedelta

def get_datetime_object(off_time, active_time):
    date_format = "%Y-%m-%d_%H-%M-%S"
    off_time = datetime.strptime(off_time, date_format)
    active_time = int(active_time)
    active_time = timedelta(seconds=active_time)
    on_time = off_time - active_time
    return on_time, off_time, active_time

