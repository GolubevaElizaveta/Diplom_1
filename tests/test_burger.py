import pytest
import allure
from praktikum.burger import Burger
from conftest import create_mock_bun, create_mock_ingredient
from data import BUN_NAME, BUN_PRICE, FILLING_NAME, FILLING_PRICE, FILLING2_NAME, FILLING2_PRICE

@allure.suite("Тестирование Burger")
class TestBurger:

    @allure.title("Проверка инициализации бургера")
    def test_create_burger(self):
        burger = Burger()
        assert (burger.bun, burger.ingredients) == (None, [])

    @allure.title("Проверка выбора булочки для бургера")
    def test_set_buns(self):
        bun = create_mock_bun()
        burger = Burger()
        burger.set_buns(bun)
        assert (burger.bun.get_name(), burger.bun.get_price()) == (BUN_NAME, BUN_PRICE)

    @allure.title("Проверка возможности добавить ингредиент в бургер")
    def test_add_ingredient(self):
        bun = create_mock_bun()
        burger = Burger()
        burger.set_buns(bun)
        ingredient = create_mock_ingredient()
        burger.add_ingredient(ingredient)
        assert (len(burger.ingredients), burger.ingredients[0].get_name(), burger.ingredients[0].get_price()) == (1, FILLING_NAME, FILLING_PRICE)

    @allure.title("Проверка возможности удалить ингредиент из бургера")
    def test_remove_ingredient(self):
        bun = create_mock_bun()
        burger = Burger()
        burger.set_buns(bun)
        ingredient = create_mock_ingredient()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    @allure.title("Проверка возможности переместить ингредиенты в бургере")
    def test_move_ingredient(self):
        bun = create_mock_bun()
        burger = Burger()
        burger.set_buns(bun)
        ingredient1 = create_mock_ingredient(name=FILLING_NAME, price=FILLING_PRICE)
        ingredient2 = create_mock_ingredient(name=FILLING2_NAME, price=FILLING2_PRICE)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].get_name() == FILLING2_NAME

    @allure.title("Проверка возможности узнать цену бургера")
    def test_get_price(self):
        bun = create_mock_bun()
        burger = Burger()
        burger.set_buns(bun)
        ingredient = create_mock_ingredient()
        burger.add_ingredient(ingredient)
        expected_price = burger.bun.get_price() * 2 + ingredient.get_price()
        assert burger.get_price() == expected_price

    @allure.title("Проверка распечатки чека")
    def test_get_receipt(self):
        bun = create_mock_bun()
        burger = Burger()
        burger.set_buns(bun)
        ingredient1 = create_mock_ingredient()
        ingredient2 = create_mock_ingredient(name=FILLING2_NAME, price=FILLING2_PRICE)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        expected_receipt = (
            f'(==== {bun.get_name()} ====)\n'
            f'= {ingredient1.get_type().lower()} {ingredient1.get_name()} =\n'
            f'= {ingredient2.get_type().lower()} {ingredient2.get_name()} =\n'
            f'(==== {bun.get_name()} ====)\n'
            f'\nPrice: {burger.get_price()}'  # Добавляем дополнительный перенос строки здесь
        )

        assert burger.get_receipt().strip() == expected_receipt
