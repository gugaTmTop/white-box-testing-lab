import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.function_solver import FunctionSolver

def test_statement_coverage():
    """Тесты для покрытия операторов"""
    solver = FunctionSolver()
    
    print("=== Тестирование покрытия операторов ===")
    
    # Тест 1: Нормальная работа (точное попадание)
    print("Тест 1: Поиск с точным попаданием")
    result = solver.find_target_point(x0=-1.8, h=0.01, epsilon=0.1)
    assert result is not None, "Точка должна быть найдена"
    print(f"Найдена точка: x={result[0]:.4f}, f(x)={result[1]:.4f}")
    
    # Тест 2: Точка не найдена
    print("\nТест 2: Точка не найдена")
    solver = FunctionSolver()
    result = solver.find_target_point(x0=10, h=1, max_iter=10)
    assert result is None, "Точка не должна быть найдена"
    print("Точка не найдена (ожидаемо)")
    
    # Тест 3: Ошибка входных данных
    print("\nТест 3: Проверка ошибки входных данных")
    try:
        solver.find_target_point(h=0)
        assert False, "Должна быть ошибка ValueError"
    except ValueError as e:
        print(f"Ошибка поймана: {e}")
    
    print("✓ Все тесты покрытия операторов пройдены!")

if __name__ == "__main__":
    test_statement_coverage()
