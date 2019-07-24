# @author Vivek
# @version 1.0
# @since 24-07-2019

from datetime import datetime

TIME_FORMAT = "%Y%m%d%H%M%S"
MILLISECONDS_MULTIPLIER = 1000


class Helper:
    def __init__(self):
        pass

    def convert_datetime_to_epoch(self, rx_datetime):
        rx_datetime = datetime.strptime(rx_datetime, TIME_FORMAT)
        return int((rx_datetime - datetime.utcfromtimestamp(0)).total_seconds() * MILLISECONDS_MULTIPLIER)

    def get_datetime(self):
        return datetime.now().strftime(TIME_FORMAT)
