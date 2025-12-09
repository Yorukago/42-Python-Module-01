class Plant:
    def __init__(self, name, height_cm, age_days):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self):
        self.height_cm += 2

    def age(self):
        self.age_days += 1

    def get_info(self):
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days old"

    def display_info(self):
        print(f"Plant name: {self.name}")
        print(f"Height: {self.height_cm}cm")
        print(f"Age: {self.age_days} days old")
        print("-" * 20)


def main():
    plant1 = Plant("Spider Lily", 75, 30)
    plant2 = Plant("Tulip", 25, 2)
    plant3 = Plant("Sunflower", 300, 95)

    garden_plants = [plant1, plant2, plant3]

    print("~ Community Garden Plant Information Board ~\n")
    for plant in garden_plants:
        plant.display_info()

    print("\nSimulating 7 days of growth...\n")

    day = 1
    while day < 7:
        for plant in garden_plants:
            plant.grow()
            plant.age()
        day += 1

    print("~ After 1 Week ~\n")
    for plant in garden_plants:
        plant.display_info()

    print("~ End of List ~\n")


if __name__ == "__main__":
    main()
