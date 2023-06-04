import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Test ADD Method
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(5, self.calc.add(5, 0))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    # Test SUBSTRACT Method
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.substract(4, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(-1, self.calc.substract(-2, -1))
        self.assertEqual(5, self.calc.substract(5, 0))

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "5", 0)
        self.assertRaises(TypeError, self.calc.substract, 6, "2")
        self.assertRaises(TypeError, self.calc.substract, "1", "0")
        self.assertRaises(TypeError, self.calc.substract, None, 3)
        self.assertRaises(TypeError, self.calc.substract, 1, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 4)
        self.assertRaises(TypeError, self.calc.substract, 8, object())

    # Test MULTIPLY Method
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "A", 0)
        self.assertRaises(TypeError, self.calc.multiply, 2, "1")
        self.assertRaises(TypeError, self.calc.multiply, "3", "3")
        self.assertRaises(TypeError, self.calc.multiply, None, 4)
        self.assertRaises(TypeError, self.calc.multiply, 5, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 1)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

    # Test DIVIDE Method
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    # Test POWER Method
    def test_power_method_returns_correct_result(self):
        self.assertEqual(100, self.calc.power(10, 2))
        self.assertEqual(0.2, self.calc.power(5, -1))
        self.assertEqual(-0.5, self.calc.power(-2, -1))
        self.assertEqual(1, self.calc.power(6, 0))

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 3)
        self.assertRaises(TypeError, self.calc.power, 3, "1")
        self.assertRaises(TypeError, self.calc.power, "2", "1")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 3)
        self.assertRaises(TypeError, self.calc.power, 7, object())

    # Test SQRT Method
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.sqrt_root(16))
        self.assertEqual(10, self.calc.sqrt_root(100))
        self.assertEqual(0, self.calc.sqrt_root(0))
        self.assertEqual(4.123105625617661, self.calc.sqrt_root(17))

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt_root, "16")
        self.assertRaises(TypeError, self.calc.sqrt_root, "A")
        self.assertRaises(TypeError, self.calc.sqrt_root, None)
        self.assertRaises(TypeError, self.calc.sqrt_root, -1)
        self.assertRaises(TypeError, self.calc.sqrt_root, object())

    # Test LOG10 Method
    def test_log_10_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.log_10(1))
        self.assertEqual(1, self.calc.log_10(10))
        self.assertEqual(0.6989700043360189, self.calc.log_10(5))

    def test_log_10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log_10, "100")
        self.assertRaises(TypeError, self.calc.log_10, 0)
        self.assertRaises(TypeError, self.calc.log_10, None)
        self.assertRaises(TypeError, self.calc.log_10, -2)
        self.assertRaises(TypeError, self.calc.log_10, object())

    # Test check_types Method - raises a TypeError when passing non-numeric parameters.
    def test_check_types_method_fails_with_non_numeric_parameters(self):
        self.assertRaises(TypeError, self.calc.check_types, "10", 1)
        self.assertRaises(TypeError, self.calc.check_types, 1, "2")
        self.assertRaises(TypeError, self.calc.check_types, "3", "4")
        self.assertRaises(TypeError, self.calc.check_types, None, 1)
        self.assertRaises(TypeError, self.calc.check_types, 2, object())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
