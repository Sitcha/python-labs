class Rocket:

    def __init__(self, weight, fuel):
        self.rocket_weight = weight + fuel
        self.fuel_weight = fuel
        self.engine_running = (fuel > 0)
    
    def spend_fuel(self, count):
        self.fuel_weight -= count
        self.rocket_weight -= count

        if self.fuel_weight > 0:
            return True

        self.fuel_weight = 0
        self.engine_running = False
        return False
    
    def get_fuel_level(self):
        return self.fuel_weight
    
    def get_total_weight(self):
        return self.rocket_weight

    def get_is_engine_running(self):
        return self.engine_running



def main():
    rocket = Rocket(1000,500)
    
    print(rocket.spend_fuel(300))
    
    print(f"the total mass of fuel is: {rocket.get_fuel_level()}")
    print(f"the rocket is currently running: {rocket.get_is_engine_running()}")
    print(f"the total current mass of the rocket is: {rocket.get_total_weight()}")
    
    print(rocket.spend_fuel(200))
    print(f"the total mass of fuel is: {rocket.get_fuel_level()}")
    print(f"the rocket is currently running: {rocket.get_is_engine_running()}")
    print(f"the total current mass of the rocket is: {rocket.get_total_weight()}")



main()

