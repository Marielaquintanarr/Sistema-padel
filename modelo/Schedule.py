class Schedule:
    next_id = 1  

    def generar_id(self):
        id_actual = Schedule.next_id  
        Schedule.next_id += 1  
        return id_actual
    
    def __init__(self, start_time, end_time):
        self.id = self.generar_id()
        self.start_time = start_time
        self.end_time = end_time
