from modelo.System import System
from modelo.Court import Court
from modelo.Player import Player

system = System()
system.create_schedule()
schedule1 = system.show_schedules()
system.create_court()
court1 = system.show_courts()

player1 = Player(1, 'Mariela', "3334510073", "Marikolas2004")

player1.make_reservation(system, "12/03/2025", schedule1, player1, court1)

player1.show_rsvs()



