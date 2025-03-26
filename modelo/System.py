from modelo.Reservation import Reservation
from modelo.Schedule import Schedule
from modelo.Court import Court

import random as rd
from datetime import datetime

class System:
    def __init__(self):
        # self.system_reservations = {dia : [[[hora_incio, hora_fin], [user, cancha, status]], [[hora_incio, hora_fin], [user, cancha, status]]]}
        self.system_reservations = {}
        self.ids = set()
        self.schedules = []
        self.courts = []
    
    def generar_id(self):
        id = rd.randint(1, 10000000)
        while id in self.ids:
            id = rd.randint(1, 10000000)
        return id

    def autorize_rsv(self, date, schedule, player, court):
        def checar_empalme():
            # checar si esta vacio
            if len(self.system_reservations) == 0 or str(date) not in self.system_reservations.keys():
                return [True, 'El system_reservations esta vacío']
            else:
                # ya existe la fecha
                max_info = len(self.system_reservations[str(date)])
                for i in range(max_info):
                    start_time = self.system_reservations[str(date)][i][0][0]
                    court_system = self.system_reservations[str(date)][i][-1][1]
                    # checar que la cancha este disponible
                    if (start_time == schedule.start_time and court_system.id == court.id) or court.status == "disable":
                        return [False, "La cancha esta disable"]
                    else:
                        return [True, "La cancha esta disponible"]

        if checar_empalme()[0] == True:
            # self.system_reservations = {dia : [[[hora_incio, hora_fin], [user, cancha, status]], [[hora_incio, hora_fin], [user, cancha, status]]], dia2 : [[[hora_incio, hora_fin], [user, cancha, status]], [[hora_incio, hora_fin], [user, cancha, status]]]}
            reservation = Reservation(self.generar_id(), player, court, date, schedule, "pendiente")
            if len(self.system_reservations) == 0 or str(reservation.date) not in self.system_reservations.keys():
                self.system_reservations[str(reservation.date)] = []
                self.system_reservations[str(reservation.date)].append([[reservation.schedule.start_time, reservation.schedule.end_time], [reservation.player.name, reservation.court.id, "pendiente"]])
                return reservation
            else:
                self.system_reservations[str(reservation.date)].append([[reservation.schedule.start_time, reservation.schedule.end_time], [reservation.player.name, reservation.court.id, "pendiente"]])
                return reservation
      
        else:
            return "No se pudo hacer la reserva"
    
    def create_schedule(self):
        start_time = input("Ingrese el Start Time: ")
        end_time = input("Ingrese el End Time: ")
        schedule = Schedule(start_time, end_time)
        self.schedules.append(schedule)
        return schedule
    
    def show_schedules(self):
        for i in range(len(self.schedules)):
            print(f'Schedule {i+1}: {self.schedules[i].start_time} - {self.schedules[i].start_time}')

        select = int(input("¿Qué horario desea?: (ej. 1,2,3): "))
        return self.schedules[select - 1]
    
    def create_court(self):
        price = int(input("Precio: "))
        status = input("Status: ")
        court = Court(price, status)
        self.courts.append(court)
        return court
    
    def show_courts(self):
        for i in range(len(self.courts)):
            print(f'Court {i+1}: Price: {self.courts[i].price} Status: {self.courts[i].status}')

        select = int(input("¿Qué cancha desea?: (ej. 1,2,3): "))
        return self.courts[select - 1]

