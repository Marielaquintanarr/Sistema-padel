from modelo.Reservation import Reservation
from modelo.Schedule import Schedule
import random as rd

class System:
    def __init__(self):
        # self.system_reservations = {dia : [[[hora_incio, hora_fin], [user, cancha, status]], [[hora_incio, hora_fin], [user, cancha, status]]]}
        self.system_reservations = {}
        self.ids = set()
    
    def generar_id(self):
        id = rd.randint(1, 10000000)
        while id in self.ids:
            id = rd.randint(1, 10000000)
        return id

    def autorize_rsv(self, schedule, player, court):
        def checar_empalme():
            # checar si esta vacio
            if len(self.system_reservations) == 0:
                return [True, 'El system_reservations esta vacío']
            else:
                # checar si ya existe la fecha
                if schedule.date in self.system_reservations.keys():
                    # si ya esta la fecha checar recorrer el dict que no sean a la misma hora
                    max_info = len(self.system_reservations[schedule.date])
                    res = True
                    for i in range(max_info):
                        start_time = self.system_reservations[schedule.date][i][0][0]
                        court_system = self.system_reservations[schedule.date][i][-1][1]
                        # checar que la cancha este disponible
                        if (start_time == schedule.start_time and court_system.id == court.id) or court.status == "disable":
                            res = False
                        else:
                            res = True

                    return [res, "La reserva se pudo guardada"]
                else:
                    return [True, 'La fecha aun no existe']
            
        if checar_empalme()[0] == True:
            # self.system_reservations = {dia : [[[hora_incio, hora_fin], [user, cancha, status]], [[hora_incio, hora_fin], [user, cancha, status]]], dia2 : [[[hora_incio, hora_fin], [user, cancha, status]], [[hora_incio, hora_fin], [user, cancha, status]]]}
            reservation = Reservation(self.generar_id(), player, court, schedule, "pendiente")
            if len(self.system_reservations) == 0:
                self.system_reservations[reservation.schedule.date] = []
                self.system_reservations[reservation.schedule.date].append([[reservation.schedule.start_time, reservation.schedule.end_time], [reservation.player.name, reservation.court.id, "pendiente"]])
                return reservation
            else:
                if reservation.schedule.date in self.system_reservations.keys():
                    self.system_reservations[reservation.schedule.date].append([[reservation.schedule.start_time, reservation.schedule.end_time], [reservation.player.name, reservation.court.id, "pendiente"]])
                    return reservation
                else:
                    self.system_reservations[reservation.schedule.date] = []
                    self.system_reservations[reservation.schedule.date].append([[reservation.schedule.start_time, reservation.schedule.end_time], [reservation.player.name, reservation.court.id, "pendiente"]])
                    return reservation
        else:
            return "No se pudo hacer la reserva"
        
    def create_schedules(self):
        
        Schedule()

