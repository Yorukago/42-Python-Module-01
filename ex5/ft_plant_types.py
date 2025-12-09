class Plant:
    def __init__(self, name, height_cm, age_days):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def display_info(self):
        print(f"Plant name: {self.name}")
        print(f"Height: {self.height_cm}cm")
        print(f"Age: {self.age_days} days old")

    def action(self):
        pass


class Flower(Plant):
    def __init__(self, name, height_cm, age_days, color):
        super().__init__(name, height_cm, age_days)
        self.color = color

    def display_info(self):
        print(
            f"{self.name} (Flower): {self.height_cm}cm, "
            f"{self.age_days} days, {self.color} color"
        )

    def bloom(self):
        print(
            f"{self.name} is blooming beautifully with "
            f"{self.color} petals!"
        )

    def action(self):
        self.bloom()


class Tree(Plant):
    def __init__(self, name, height_cm, age_days, trunk_diameter):
        super().__init__(name, height_cm, age_days)
        self.trunk_diameter = trunk_diameter

    def display_info(self):
        print(
            f"{self.name} (Tree): {self.height_cm}cm, "
            f"{self.age_days} days, {self.trunk_diameter}cm diameter"
        )

    def produce_shade(self):
        shade_area = self.trunk_diameter * 1.50
        print(
            f"{self.name} provides about "
            f"{shade_area:.1f} square meters of shade"
        )

    def action(self):
        self.produce_shade()


class Vegetable(Plant):
    def __init__(
        self,
        name,
        height_cm,
        age_days,
        harvest_season,
        nutricional_value
    ):
        super().__init__(name, height_cm, age_days)
        self.harvest_season = harvest_season
        self.nutricional_value = nutricional_value

    def display_info(self):
        print(
            f"{self.name} (Vegetable): {self.height_cm}cm, "
            f"{self.age_days} days, {self.harvest_season} harvest"
        )

    def show_nutrition(self):
        print(
            f"{self.name} is rich in {self.nutricional_value} "
            f"and is harvested in {self.harvest_season}"
        )

    def action(self):
        self.show_nutrition()


def main():
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 30, 40, "red")
    tulip = Flower("Tulip", 20, 15, "yellow")

    oak = Tree("Oak", 500, 2000, 80)
    pine = Tree("Pine", 450, 1500, 60)

    carrot = Vegetable("Carrot", 15, 50, "Spring", "vitamin A")
    lettuce = Vegetable("Lettuce", 10, 25, "Summer", "fiber")

    garden = [rose, tulip, oak, pine, carrot, lettuce]

    for plant in garden:
        plant.display_info()
        plant.action()
        print()


if __name__ == "__main__":
    main()
