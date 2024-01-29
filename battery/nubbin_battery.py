from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        should_service_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if should_service_date < self.current_date:
            return True
        else:
            return False