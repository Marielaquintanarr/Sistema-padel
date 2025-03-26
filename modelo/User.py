from abc import ABC, abstractclassmethod

class User(ABC):
    def __init__(self, id, name, phone, password):
        self.id = id
        self.name = name
        self.phone = phone
        self.password = password


