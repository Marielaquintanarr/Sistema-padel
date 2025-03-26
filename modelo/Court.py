
class Court:
    def __init__(self, price, status):
        self.price = price
        self.status = status
    
    def to_dict(self):
        return {
            "price": self.price,
            "status": self.status
        }