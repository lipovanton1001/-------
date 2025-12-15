import pytest
from app import calculate_scholarship

# 1. Тест успішних сценаріїв (3 в 1)
@pytest.mark.parametrize("grade, max_g, base, expected", [
    (4.5, 5, 2000, 1800.0), # Звичайний розрахунок
    (5.0, 5, 1000, 1000.0), # Максимальний бал
    (0.0, 5, 2000, 0.0),    # Нульовий бал
])
def test_success(grade, max_g, base, expected):
    assert calculate_scholarship(grade, max_g, base) == expected

# 2. Тест помилок (5 в 1)
@pytest.mark.parametrize("grade, max_g, base, error_type", [
    (6.0, 5, 2000, ValueError), # Бал більший за макс
    (-1,  5, 2000, ValueError), # Негативний бал
    (4,   0, 2000, ValueError), # Макс бал 0
    (4,   5, -100, ValueError), # База негативна
    ("A", 5, 2000, TypeError),  # Літера замість цифри
])
def test_errors(grade, max_g, base, error_type):
    with pytest.raises(error_type):
        calculate_scholarship(grade, max_g, base)