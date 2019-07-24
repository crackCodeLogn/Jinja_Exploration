# @author Vivek
# @version 1.0
# @since 24-07-2019
from datetime import datetime

from Helper import Helper


class Core:
    sid = "12345"
    name = "ZOMBIE"
    start_time = datetime.utcnow()
    end_time = datetime.utcnow()
    diff_time = 0
    helper = Helper()

    def __init__(self, sid, name, start_time, end_time, **kwargs):
        self.sid = sid
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

        self.create_diff_time(self.start_time, self.end_time)

    def create_diff_time(self, start, end):
        start = self.helper.convert_datetime_to_epoch(start)
        end = self.helper.convert_datetime_to_epoch(end)
        self.diff_time = end - start

    def __eq__(self, other):
        return self.sid == other.sid

    def __repr__(self):
        return str(
            "[SID : {sid} => Name='{name}', Start time {start}, End time {end}, difference {diff}]".format(sid=self.sid,
                                                                                                           name=self.name,
                                                                                                           start=self.start_time,
                                                                                                           end=self.end_time,
                                                                                                           diff=self.diff_time))
