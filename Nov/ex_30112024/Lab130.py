class Car:
    def __init__(self,o_name,o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model
    def start_engine(self):
        print(f"Name {self.name}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
jaguar = Car("Jaguar","X671",2023)
landrover = Car("Defender", "L481",2024)
jaguar.start_engine()
print("______________")
landrover.start_engine()

