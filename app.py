class InvalidGradeError(Exception):
    """Виключення для некоректного балу"""
    pass

class InvalidScholarshipError(Exception):
    """Виключення для некоректної базової стипендії"""
    pass

def calculate_scholarship(student_grade, max_grade, base_scholarship):
    """
    Розраховує розмір стипендії студента.
    
    Параметри:
    student_grade (float): Середній бал студента
    max_grade (float): Максимальний можливий бал
    base_scholarship (float): Базова сума стипендії
    
    Повертає:
    float: Розрахований розмір стипендії
    
    Генерує виключення:
    InvalidGradeError: Якщо бали некоректні
    InvalidScholarshipError: Якщо базова стипендія некоректна
    """
    
    # Перевірка балу студента
    if not isinstance(student_grade, (int, float)):
        raise InvalidGradeError("Бал студента має бути числом")
    
    if student_grade < 0:
        raise InvalidGradeError("Бал студента не може бути від'ємним")
    
    if student_grade > max_grade:
        raise InvalidGradeError(f"Бал студента ({student_grade}) не може перевищувати максимальний бал ({max_grade})")
    
    # Перевірка максимального балу
    if not isinstance(max_grade, (int, float)):
        raise InvalidGradeError("Максимальний бал має бути числом")
    
    if max_grade <= 0:
        raise InvalidGradeError("Максимальний бал має бути додатнім числом")
    
    # Перевірка базової стипендії
    if not isinstance(base_scholarship, (int, float)):
        raise InvalidScholarshipError("Базова стипендія має бути числом")
    
    if base_scholarship <= 0:
        raise InvalidScholarshipError("Базова стипендія має бути додатнім числом")
    
    # Розрахунок стипендії
    percentage = student_grade / max_grade
    scholarship = percentage * base_scholarship
    
    return scholarship

def main():
    """Головна функція програми"""
    print("=" * 50)
    print("  КАЛЬКУЛЯТОР СТИПЕНДІЇ СТУДЕНТА")
    print("=" * 50)
    print()
    
    try:
        # Введення даних
        student_grade = float(input("Введіть середній бал студента: "))
        max_grade = float(input("Введіть максимальний можливий бал: "))
        base_scholarship = float(input("Введіть базову суму стипендії (грн): "))
        
        # Розрахунок стипендії
        scholarship = calculate_scholarship(student_grade, max_grade, base_scholarship)
        
        # Виведення результату
        percentage = (student_grade / max_grade) * 100
        print()
        print("-" * 50)
        print(f"Середній бал: {student_grade}/{max_grade}")
        print(f"Відсоток від максимального балу: {percentage:.2f}%")
        print(f"Базова стипендія: {base_scholarship:.2f} грн")
        print(f"Розрахована стипендія: {scholarship:.2f} грн")
        print("-" * 50)
        
    except ValueError:
        print("\n❌ ПОМИЛКА: Введено некоректне значення. Будь ласка, введіть число.")
    except InvalidGradeError as e:
        print(f"\n❌ ПОМИЛКА БАЛУ: {e}")
    except InvalidScholarshipError as e:
        print(f"\n❌ ПОМИЛКА СТИПЕНДІЇ: {e}")
    except Exception as e:
        print(f"\n❌ НЕПЕРЕДБАЧЕНА ПОМИЛКА: {e}")

if __name__ == "__main__":
    main()
    
    print("\n" + "=" * 50)
    print("  ПРИКЛАДИ ВИКОРИСТАННЯ")
    print("=" * 50)
    
    test_cases = [
        (4.5, 5.0, 2000, "Відмінний студент"),
        (3.0, 5.0, 2000, "Середній студент"),
        (5.0, 5.0, 2000, "Максимальний бал"),
    ]
    
    for grade, max_g, base, description in test_cases:
        try:
            result = calculate_scholarship(grade, max_g, base)
            print(f"\n{description}: {grade}/{max_g} = {result:.2f} грн")
        except Exception as e:
            print(f"\n{description}: Помилка - {e}")