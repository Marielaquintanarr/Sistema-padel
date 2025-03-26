from modelo.System import System
from modelo.Schedule import Schedule
from modelo.Court import Court
from modelo.Player import Player

system = System()
schedule1 = Schedule(1, "12/03/2025", "8:00PM", "9:00PM")
schedule2 = Schedule(2, "13/03/2025", "4:00PM", "5:00PM")
schedule3 = Schedule(3, "12/03/2025", "7:00PM", "8:00PM")

court1 = Court(1, 950, "Disponible")
court2 = Court(2, 950, "Disponible")
player1 = Player(1, 'Mariela', "3334510073", "Marikolas2004")

player1.make_reservation(system, schedule1, player1, court1)
player1.make_reservation(system, schedule2, player1, court2)
player1.make_reservation(system, schedule3, player1, court1)
player1.show_rsvs()



