import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    teste1 = Dish("Bolo", 17.0)
    teste2 = Dish("Bolo", 17.0)
    teste3 = Dish("Pizza", 25.0)

    assert teste1.name == "Bolo"
    assert teste3.name == "Pizza"

    assert hash(teste1) == hash(teste2)
    assert hash(teste1) != hash(teste3)

    assert teste1 == teste2
    assert teste1 != teste3

    assert repr(teste1) == "Dish('Bolo', R$17.00)"

    with pytest.raises(TypeError):
        Dish("Bolo de cenoura", "19.00")
    with pytest.raises(ValueError):
        Dish("Bolo de cenoura", -19.00)

    teste1.add_ingredient_dependency(Ingredient("farinha"), 1)
    assert teste1.get_restrictions() == {Restriction.GLUTEN}

    teste1.add_ingredient_dependency(Ingredient("ovo"), 1)
    assert teste1.get_ingredients() == {
        Ingredient("farinha"), Ingredient("ovo")
    }
