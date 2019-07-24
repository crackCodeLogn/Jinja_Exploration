# @author Vivek
# @version 1.0
# @since 24-07-2019

import random
import string
import time

from Core import Core
from Helper import Helper
from HtmlGenerator import HtmlGenerator


class MainActivity:
    def __init__(self):
        self.helper = Helper()
        self.sid_list = []
        self.core_list = []
        pass

    def generate_random_core(self, cores, upper_time_delay):
        for i in range(1, cores + 1, 1):
            sid = self.generate_unique_sid()
            name = self.generate_random_name(10)
            start_time = self.generate_start_time()
            time.sleep(random.randrange(1, upper_time_delay + 1, 1))
            end_time = self.generate_end_time()

            core = Core(sid, name, start_time, end_time)
            self.core_list.append(core)
            print(core)

    def generate_unique_sid(self):
        sid = self.generate_random_sid(5)
        while sid in self.sid_list:
            print("sid already present, skipping it : " + str(sid))
            sid = self.generate_random_sid(5)
        self.sid_list.append(sid)
        return sid

    def generate_random_sid(self, digits):
        lower = pow(10, digits - 1)
        upper = pow(10, digits)
        return random.randrange(lower, upper, 1)

    def generate_random_name(self, length):
        name = ""
        for i in range(1, length, 1):
            name += random.choice(string.ascii_letters)
        return name

    def generate_start_time(self):
        return self.helper.get_datetime()

    def generate_end_time(self):
        return self.helper.get_datetime()


if __name__ == '__main__':
    starter = MainActivity()
    starter.generate_random_core(cores=10, upper_time_delay=2)
    html_gen = HtmlGenerator()
    print(html_gen.generate_html_from_template(starter.core_list))
