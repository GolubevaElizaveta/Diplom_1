import pytest
import allure
from conftest import create_mock_bun
from data import BUN_NAME, BUN_PRICE

@allure.suite("Тестирование Bun")
class TestBun:

    @pytest.fixture
    def bun(self):
        return create_mock_bun(BUN_NAME, BUN_PRICE)

    @allure.title("Проверка имени и цены булочки")
    def test_get_name_and_price(self, bun):
        result = (bun.get_name(), bun.get_price())
        assert result == (BUN_NAME, BUN_PRICE)

    @pytest.mark.parametrize("name, price", [
        ("Булочка с кунжутом", 60.0),
        ("Чиабатта", 70.0),
        ("Ржаная булочка", 65.0)  # Новая булочка
    ])
    @allure.title("Проверка создания булочек с параметризацией")
    def test_bun_creation(self, name, price):
        bun = create_mock_bun(name, price)
        result = (bun.get_name(), bun.get_price())
        assert result == (name, price)


