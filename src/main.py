# src/main.py
#Проверка
from task import Task
from task_manager import TaskManager

def main():
    manager = TaskManager()

    # Пример добавления задач
    task1 = Task("Купить продукты", "Купить молоко и хлеб.")
    task2 = Task("Позвонить другу", "Позвонить и обсудить планы.")

    manager.add_task(task1)
    manager.add_task(task2)

    # Вывод списка задач
    print("Список задач:")
    manager.display_tasks()

    # Завершение задачи
    task1.mark_completed()

    # Обновление описания
    task2.update_description("Позвонить другу и обсудить путешествие.")

    # Удаление задачи
    manager.remove_task("Купить продукты")

    print("\nОбновлённый список задач:")
    manager.display_tasks()

if __name__ == "__main__":
    main()
