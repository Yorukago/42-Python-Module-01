class Plant:
    def __init__(self, name, height_cm, age_days):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def display_info(self):
        print(f"Plant name: {self.name}")
        print(f"Height: {self.height_cm}cm")
        print(f"Age: {self.age_days} days old")
        print("-" * 20)


def main():
    plant_data = [
        ("Marigold", 18, 12),
        ("Rose", 35, 45),
        ("Daisy", 22, 28),
        ("Lavender", 40, 60),
        ("Orchid", 15, 5)
    ]

    garden_plants = []

    print("=== Plant Factory Output ===")

    for name, height, age in plant_data:
        new_plant = Plant(name, height, age)
        garden_plants.append(new_plant)
        print(f"Created: {name} ({height}cm, {age} days)")
    print(f"\nTotal plants created: {len(garden_plants)}\n")

    print("=== Plant Info Board ===")
    for plant in garden_plants:
        plant.display_info()
    print("=== End of List ===")


if __name__ == "__main__":
    main()
