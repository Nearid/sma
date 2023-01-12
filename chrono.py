import time

class Chrono:

    @staticmethod
    def has_one_sec_passed(timestamp):
        if time.time() - timestamp >= 1000:
            Chrono.currentTime = time.time()
            return True
        return False
