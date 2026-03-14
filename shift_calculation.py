import datetime
import os

def calculate_shift():
    """
    Основная функция: расчет выполнения сменного задания
    """
    print("=" * 50)
    print("     Система расчета выполнения сменного задания")
    print("=" * 50)
    
    # 1. Получение ввода от пользователя
    try:
        product_name = input("Введите название продукта: ")
        plan = float(input("Введите плановое задание (тонн): "))
        fact = float(input("Введите фактическое производство (тонн): "))
    except ValueError:
        print("Ошибка: Введите корректное число!")
        return
    
    # 2. Проверка ввода
    if plan <= 0:
        print("Ошибка: Плановое задание должно быть больше 0!")
        return
    
    # 3. Расчет процента выполнения
    percent = (fact / plan) * 100
    
    # 4. Определение статуса выполнения
    if percent >= 100:
        status = "✓ План выполнен"
        result_text = "Выполнен"
    else:
        status = "✗ План не выполнен"
        result_text = "Не выполнен"
    
    # 5. Вывод результатов
    print("\n" + "-" * 30)
    print(f"Продукт: {product_name}")
    print(f"План: {plan:.2f} тонн")
    print(f"Факт: {fact:.2f} тонн")
    print(f"Процент выполнения: {percent:.2f}%")
    print(f"Результат: {status}")
    print("-" * 30)
    
    # 6. Запись в файл
    save_to_file(product_name, plan, fact, percent, result_text)

def save_to_file(product, plan, fact, percent, result):
    """
    Сохранение результатов в файл
    """
    filename = "shift_report.txt"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Проверка существования файла, если нет - создать с заголовком
    write_header = not os.path.exists(filename) or os.path.getsize(filename) == 0
    
    try:
        with open(filename, "a", encoding="utf-8") as file:
            if write_header:
                file.write("=" * 80 + "\n")
                file.write("                 Отчет о выполнении сменных заданий\n")
                file.write("=" * 80 + "\n")
                file.write(f"{'Дата и время':<20} {'Продукт':<15} {'План(т)':<12} {'Факт(т)':<12} {'% выполн':<10} {'Результат':<10}\n")
                file.write("-" * 80 + "\n")
            
            # Запись строки данных
            line = f"{current_time:<20} {product:<15} {plan:<12.2f} {fact:<12.2f} {percent:<10.2f} {result:<10}\n"
            file.write(line)
            
        print(f"\n✅ Результат сохранен в файл: {filename}")
        print(f"Расположение файла: {os.path.abspath(filename)}")
        
    except Exception as e:
        print(f"\n❌ Ошибка при сохранении файла: {e}")

def view_report():
    """
    Просмотр содержимого файла отчета
    """
    filename = "shift_report.txt"
    
    if not os.path.exists(filename):
        print("Файл отчета не существует. Сначала выполните расчет.")
        return
    
    try:
        print("\n" + "=" * 50)
        print("Содержимое отчета о сменных заданиях")
        print("=" * 50)
        
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
            
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

def main():
    """
    Главное меню
    """
    while True:
        print("\n" + "=" * 50)
        print("         Система расчета сменных заданий - Главное меню")
        print("=" * 50)
        print("1. Рассчитать новую смену")
        print("2. Просмотреть историю отчетов")
        print("3. Выход из программы")
        print("-" * 50)
        
        choice = input("Выберите действие (1-3): ")
        
        if choice == "1":
            calculate_shift()
        elif choice == "2":
            view_report()
        elif choice == "3":
            print("Спасибо за использование программы, до свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

# Точка входа в программу
if __name__ == "__main__":
    main()