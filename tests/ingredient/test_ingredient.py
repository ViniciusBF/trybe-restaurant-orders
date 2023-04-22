from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    teste1 = Ingredient("bacon")
    teste2 = Ingredient("farinha")
    teste3 = Ingredient("bacon")

    assert repr(teste1) == "Ingredient('bacon')"
    assert teste1.name == "bacon"
    assert repr(teste2) == "Ingredient('farinha')"
    assert teste2.name == "farinha"

    assert teste1 == teste3
    assert len(teste1.restrictions) == 2

    assert hash(teste1) == hash(teste3)
    assert hash(teste1) != hash(teste2)
