# src/task_manager.py
#проверка
from task import Task
from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        """Добавить задачу в менеджер."""
        self.tasks.append(task)

    def remove_task(self, title: str):
        """Удалить задачу по названию."""
        self._validate_task_existence(title)
        self.tasks = [task for task in self.tasks if task.title != title]

    def display_tasks(self):
        """Вывести список всех задач."""
        for task in self.tasks:
            print(task)

    def _validate_task_existence(self, title: str):
        """Проверка существования задачи (protected)."""
        if not any(task.title == title for task in self.tasks):
            raise ValueError("Задача с таким названием не найдена.")
