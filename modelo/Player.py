from modelo.User import User
from modelo.Reservation import Reservation

class Player(User):
    def __init__(self, id, name, phone, password):
        super().__init__(id, name, phone, password)
        # reservaciones = {date : [court, start_time, end_time]}
        self.reservations = {}
    
    def make_reservation(self, system, schedule, player, court):
        #reservation = {id : [self.schedule.date, self.schedule.start_time, self.schedule.end_time, self.user.name, self.court.id, self.status]
        # se obtiene una rsv
        reservation = system.autorize_rsv(schedule, player, court)

        if isinstance(reservation, Reservation):
            if len(self.reservations) == 0:
                self.reservations[reservation.schedule.date] = []
                self.reservations[reservation.schedule.date].append([reservation.court.id, reservation.schedule.start_time, reservation.schedule.end_time])
            else:
                if reservation.schedule.date in self.reservations.keys():
                    self.reservations[reservation.schedule.date].append([reservation.court.id, reservation.schedule.start_time, reservation.schedule.end_time])
                else:
                    self.reservations[reservation.schedule.date] = []
                    self.reservations[reservation.schedule.date].append([reservation.court.id, reservation.schedule.start_time, reservation.schedule.end_time])

        else:
            print("Error en la reserva:", reservation)
    
    def show_rsvs(self):
        print(self.reservations)







