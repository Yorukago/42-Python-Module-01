# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jzorreta <jzorreta@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 15:54:35 by jzorreta          #+#    #+#              #
#    Updated: 2025/12/08 15:56:33 by jzorreta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class SecurePlant:
    def __init__(self, name, height_cm, age_days):
        self.name = name
        self.__height_cm = 0
        self.__age_days = 0

        self.set_height(height_cm)
        self.set_age(age_days)

    def get_height(self):
        return self.__height_cm

    def get_age(self):
        return self.__age_days

    def set_height(self, new_height):
        if new_height < 0:
            print("Error: Height cannot be negative!")
        else:
            self.__height_cm = new_height

    def set_age(self, new_age):
        if new_age < 0:
            print("Error: Age cannot be negative!")
        else:
            self.__age_days = new_age


    def display_info(self):
        print(f"SecurePlant: {self.name}")
        print(f"Height: {self.__height_cm}cm")
        print(f"Age: {self.__age_days} days")

def main():
    plant = SecurePlant("Lavender", 30, 20)
    plant.display_info()

    print("\nTrying some invalid updates...\n")

    plant.set_height(-10)
    plant.set_age(-5)

    plant.set_height(42)
    plant.set_age(25)

    plant.display_info()

if __name__ == "__main__":
    main()
