import pytest
import allure
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@allure.suite("Тестирование Database")
class TestDatabase:

    @pytest.fixture
    def database(self):
        db = Database()  # Создаем экземпляр Database
        return db  # Возвращаем его, инициализация произойдет в __init__

    @allure.title("Проверка инициализации булочек и ингредиентов")
    def test_init(self, database):
        # Проверяем булочки
        buns = database.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

        # Проверяем ингредиенты
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[3].get_name() == "cutlet"

    @pytest.mark.parametrize("bun_name, bun_price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    @allure.title("Проверка булочек с параметризацией")
    def test_bun_parametrization(self, database, bun_name, bun_price):
        buns = database.available_buns()
        assert any(bun.get_name() == bun_name and bun.get_price() == bun_price for bun in buns)

    @pytest.mark.parametrize("ingredient_type, ingredient_name", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce"),
        (INGREDIENT_TYPE_FILLING, "cutlet")
    ])
    @allure.title("Проверка ингредиентов с параметризацией")
    def test_ingredient_parametrization(self, database, ingredient_type, ingredient_name):
        ingredients = database.available_ingredients()
        assert any(
            ingredient.get_type() == ingredient_type and ingredient.get_name() == ingredient_name for ingredient in
            ingredients)
