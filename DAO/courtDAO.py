from modelo.db import db
from modelo.Court import Court

class courtDAO:
    @staticmethod
    def insertar(court: Court):
        try:
            response = db.table("courts").insert(court.to_dict()).execute()
            print(response)
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False
