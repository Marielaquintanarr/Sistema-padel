from DAO.courtDAO import courtDAO
from flask import request

from modelo.Court import Court

def insertarCourt(price, status):
    # Usamos los datos recibidos en la solicitud
    court = Court(price, status)
    if courtDAO.insertar(court):
        return True
    else:
        return False
