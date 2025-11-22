import sys
import os

def run_all_tests():
    """Запуск всех тестов"""
    test_files = [
        'tests/test_statement_coverage.py',
        'tests/test_decision_coverage.py', 
        'tests/test_condition_coverage.py',
        'tests/test_combination_coverage.py'
    ]
    
    for test_file in test_files:
        if os.path.exists(test_file):
            print(f"\n{'='*50}")
            print(f"Запуск {test_file}")
            print('='*50)
            os.system(f'python {test_file}')
        else:
            print(f"Файл {test_file} не найден")

if __name__ == "__main__":
    run_all_tests()
