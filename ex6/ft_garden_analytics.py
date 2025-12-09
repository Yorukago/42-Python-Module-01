class Plant:
    def __init__(self, name, height_cm, age_days):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, amount=1):
        self.height_cm += amount
        print(f"{self.name} grew {amount}cm")

    def display_info(self):
        print(f"- {self.name}: {self.height_cm}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height_cm, age_days, color):
        super().__init__(name, height_cm, age_days)
        self.color = color

    def bloom(self):
        return "(blooming)"

    def display_info(self):
        print(
            f"- {self.name}: {self.height_cm}cm, "
            f"{self.color} flowers {self.bloom()}"
        )


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height_cm, age_days, color, prize_points):
        super().__init__(name, height_cm, age_days, color)
        self.prize_points = prize_points

    def display_info(self):
        print(
            f"- {self.name}: {self.height_cm}cm, "
            f"{self.color} flowers {self.bloom()}, "
            f"Prize points: {self.prize_points}"
        )


class GardenManager:

    total_gardens = 0

    class GardenStats:
        def __init__(self, plants):
            self.plants = plants

        def calculate_plant_types(self):
            regular = sum(
                1 for p in self.plants
                if type(p) is Plant
            )
            flowering = sum(
                    1 for p in self.plants
                    if type(p) is FloweringPlant
                )
            prize = sum(
                    1 for p in self.plants
                    if type(p) is PrizeFlower
                )
            return regular, flowering, prize

        def check_height_validation(self):
            return all(p.height_cm > 0 for p in self.plants)

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.total_growth = 0
        self.stats_helper = GardenManager.GardenStats(self.plants)
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.display_info()

        regular, flowering, prize = self.stats_helper.calculate_plant_types()
        height_ok = self.stats_helper.check_height_validation()

        print(
            f"Plants added: {len(self.plants)}, "
            f"Total growth: {self.total_growth}cm"
        )
        print(
            f"Plant types: {regular} regular, "
            f"{flowering} flowering, {prize} prize flowers"
        )
        print(f"Height validation test: {height_ok}")

    @classmethod
    def create_garden_network(cls):
        alice = cls("Alice")
        bob = cls("Bob")
        print(f"Total gardens managed: {cls.total_gardens}")
        return [alice, bob]

    @staticmethod
    def calculate_environmental_factor(temp_celsius, humidity_percent):
        return (temp_celsius * 0.5) + (humidity_percent * 0.1)


def main():
    print("=== Garden Management System Demo ===")

    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 40, "red")
    sunflower = PrizeFlower("Sunflower", 50, 90, "yellow", 10)

    alice_garden = GardenManager("Alice")
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.grow_all()
    alice_garden.report()

    GardenManager.create_garden_network()


if __name__ == "__main__":
    main()
