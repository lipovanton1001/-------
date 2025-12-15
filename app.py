def calculate_scholarship(grade, max_grade, base):
    # Перевірка типів (всі аргументи мають бути числами)
    if not all(isinstance(x, (int, float)) for x in [grade, max_grade, base]):
        raise TypeError("Всі дані мають бути числами")
    
    # Перевірка логіки (межі балів та додатна стипендія)
    if not (0 <= grade <= max_grade and max_grade > 0 and base > 0):
        raise ValueError("Некоректні значення: перевірте межі балів та суму")

    return (grade / max_grade) * base

if __name__ == "__main__":
    # Список тестів: (бал, макс, база)
    tests = [
        (4.5, 5, 2000),  # Ок
        (3.0, 5, 2000),  # Ок
        (6.0, 5, 2000),  # Помилка: бал > макс
        (-1, 5, 2000),   # Помилка: від'ємний бал
        ("A", 5, 2000)   # Помилка: не число
    ]

    print("--- Результати розрахунків ---")
    for args in tests:
        try:
            # *args розпаковує кортеж у аргументи функції
            result = calculate_scholarship(*args)
            print(f"Вхід: {args} -> Стипендія: {result:.2f} грн")
        except Exception as e:
            print(f"Вхід: {args} -> Помилка: {e}")