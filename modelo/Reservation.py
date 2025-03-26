
class Reservation:
    def __init__(self, id, player, court, schedule, status):
        self.id = id
        self.player = player
        self.court = court
        # schedule = [date, start_time, end_time]
        self.schedule = schedule
        self.status = status
        