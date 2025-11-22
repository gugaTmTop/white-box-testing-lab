from function_solver import FunctionSolver

def main():
    print("=== Поиск точки функции f(x) = x^2 - e^x = -10 ===")
    solver = FunctionSolver()
    
    try:
        # Ввод данных
        x0 = float(input("Введите начальное значение X0: "))
        h = float(input("Введите шаг h: "))
        
        # Поиск точки
        result = solver.find_target_point(x0=x0, h=h)
        
        if result:
            x, fx, iterations = result
            print(f"\nРезультат:")
            print(f"Найдена точка: x = {x:.6f}")
            print(f"Значение функции: f(x) = {fx:.6f}")
            print(f"Отклонение от -10: {abs(fx + 10):.8f}")
            print(f"Количество вызовов функции: {solver.call_count}")
        else:
            print("Точка не найдена в заданном диапазоне")
            
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Ошибка выполнения: {e}")

if __name__ == "__main__":
    main()
