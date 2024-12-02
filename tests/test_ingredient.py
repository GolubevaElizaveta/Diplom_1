import pytest
import allure
from conftest import create_mock_ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@allure.suite("Тестирование Ingredient")
class TestIngredient:

    @pytest.fixture
    def ingredient(self):
        return create_mock_ingredient(name="Hot Sauce", price=100.0, ingredient_type=INGREDIENT_TYPE_SAUCE)

    @allure.title("Проверка инициализации ингредиента")
    def test_initialization(self, ingredient):
        assert (ingredient.get_type(), ingredient.get_name(), ingredient.get_price()) == (
            INGREDIENT_TYPE_SAUCE, "Hot Sauce", 100.0
        )

    @allure.title("Проверка метода get_type")
    def test_get_type(self, ingredient):
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    @allure.title("Проверка метода get_name")
    def test_get_name(self, ingredient):
        assert ingredient.get_name() == "Hot Sauce"

    @allure.title("Проверка метода get_price")
    def test_get_price(self, ingredient):
        assert ingredient.get_price() == 100.0

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Sour Cream", 150.0),
        (INGREDIENT_TYPE_FILLING, "Cutlet", 200.0),
        (INGREDIENT_TYPE_FILLING, "Dinosaur", 250.0)
    ])
    @allure.title("Проверка ингредиентов с параметризацией")
    def test_ingredient_parametrization(self, ingredient_type, name, price):
        ingredient = create_mock_ingredient(name, price, ingredient_type)
        assert (ingredient.get_type(), ingredient.get_name(), ingredient.get_price()) == (
            ingredient_type, name, price
        )

