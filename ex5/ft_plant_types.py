#!/usr/bin/env python3

class Plant:
    """Base class for all garden plants."""

    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        """Initialize common plant attributes."""
        self.name: str = name
        self.height_cm: int = height_cm
        self.age_days: int = age_days

    def display_info(self) -> None:
        """Display basic info."""
        print(f"Plant name: {self.name}")
        print(f"Height: {self.height_cm}cm")
        print(f"Age: {self.age_days} days old")

    def action(self) -> None:
        """Generic action to be overridden by subclasses."""
        pass


class Flower(Plant):
    """Specialized plant with color and blooming behavior."""

    def __init__(self, name: str, h: int, a: int, color: str) -> None:
        """Use super() to setup basic attributes then add color."""
        super().__init__(name, h, a)
        self.color: str = color

    def display_info(self) -> None:
        """Override display to include color."""
        print(f"{self.name} (Flower): {self.height_cm}cm, "
              f"{self.age_days} days, {self.color} color")

    def bloom(self) -> None:
        """Unique flower behavior."""
        print(f"{self.name} is blooming beautifully with "
              f"{self.color} petals!")

    def action(self) -> None:
        """Map action to blooming."""
        self.bloom()


class Tree(Plant):
    """Specialized plant with trunk diameter and shade behavior."""

    def __init__(self, name: str, h: int, a: int, trunk_dia: float) -> None:
        """Setup parent attributes and trunk diameter."""
        super().__init__(name, h, a)
        self.trunk_diameter: float = trunk_dia

    def display_info(self) -> None:
        """Override display to include trunk size."""
        print(f"{self.name} (Tree): {self.height_cm}cm, "
              f"{self.age_days} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """Calculate and display shade area."""
        shade_area: float = self.trunk_diameter * 1.50
        print(f"{self.name} provides about "
              f"{shade_area:.1f} square meters of shade")

    def action(self) -> None:
        """Map action to shade production."""
        self.produce_shade()


class Vegetable(Plant):
    """Specialized plant with harvest info and nutrition."""

    def __init__(self, name: str, h: int, a: int, season: str,
                 nut: str) -> None:
        """Setup parent attributes and nutritional info."""
        super().__init__(name, h, a)
        self.harvest_season: str = season
        self.nutritional_value: str = nut

    def display_info(self) -> None:
        """Override display to include harvest info."""
        print(f"{self.name} (Vegetable): {self.height_cm}cm, "
              f"{self.age_days} days, {self.harvest_season} harvest")

    def show_nutrition(self) -> None:
        """Display nutritional facts."""
        print(f"{self.name} is rich in {self.nutritional_value} "
              f"and is harvested in {self.harvest_season}")

    def action(self) -> None:
        """Map action to nutrition display."""
        self.show_nutrition()


def main() -> None:
    """The main garden setup demonstrating polymorphism."""
    print("=== Community Garden Plant Types ===\n")

    # Creating 2 instances of each as required
    rose = Flower("Rose", 30, 40, "red")
    tulip = Flower("Tulip", 20, 15, "yellow")

    oak = Tree("Oak", 500, 2000, 80.0)
    pine = Tree("Pine", 450, 1500, 60.0)

    carrot = Vegetable("Carrot", 15, 50, "Spring", "vitamin A")
    lettuce = Vegetable("Lettuce", 10, 25, "Summer", "fiber")

    garden: list[Plant] = [rose, tulip, oak, pine, carrot, lettuce]

    # Streamlined loop using polymorphism
    for plant in garden:
        plant.display_info()
        plant.action()
        print()


if __name__ == "__main__":
    main()
