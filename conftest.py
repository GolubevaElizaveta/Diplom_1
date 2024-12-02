from unittest.mock import Mock
import allure
import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@allure.step("Создание мока для булочки")
def create_mock_bun(name="Фокачча", price=55.0):
    mock_bun = Mock(spec=Bun)
    mock_bun.get_name.return_value = name
    mock_bun.get_price.return_value = price
    return mock_bun

@allure.step("Создание мока для ингредиента")
def create_mock_ingredient(name="Курица BBQ", price=40.0, ingredient_type="начинка"):
    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_name.return_value = name
    mock_ingredient.get_price.return_value = price
    mock_ingredient.get_type.return_value = ingredient_type
    return mock_ingredient

@pytest.fixture
def burger():
    b = Burger()
    b.set_buns(create_mock_bun())
    return b

@pytest.fixture
def ingredient():
    return create_mock_ingredient()
