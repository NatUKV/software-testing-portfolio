import pytest
from src.order_calculator import OrderCalculator


class TestOrderCalculator:

    def setup_method(self):
        self.calculator = OrderCalculator()

    def test_calculate_total_without_discount(self):
        result = self.calculator.calculate_total(price=10, quantity=2)
        assert result == 20

    def test_calculate_total_with_discount(self):
        result = self.calculator.calculate_total(price=50, quantity=2, discount_rate=10)
        assert result == 90

    def test_calculate_total_with_decimal_price(self):
        result = self.calculator.calculate_total(price=9.99, quantity=3)
        assert result == 29.97

    def test_negative_price_should_raise_error(self):
        with pytest.raises(ValueError, match="Price cannot be negative"):
            self.calculator.calculate_total(price=-5, quantity=1)

    def test_zero_quantity_should_raise_error(self):
        with pytest.raises(ValueError, match="Quantity must be greater than zero"):
            self.calculator.calculate_total(price=10, quantity=0)

    def test_invalid_discount_rate_should_raise_error(self):
        with pytest.raises(ValueError, match="Discount rate must be between 0 and 100"):
            self.calculator.calculate_total(price=10, quantity=1, discount_rate=150)

