import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, "r") as source:
            self.__data__ = list(csv.DictReader(source))

        dishes = {}

        for row in self.__data__:
            dish = Dish(row['dish'], float(row['price']))
            if row["dish"] not in dishes:
                dishes[row['dish']] = dish

            dishes[row['dish']].add_ingredient_dependency(
                Ingredient(row['ingredient']), int(row['recipe_amount'])
            )

        self.dishes = set(dishes.values())
