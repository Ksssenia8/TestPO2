# src/task.py

class Task:
    def __init__(self, title: str, description: str, status: str = "pending"):
        self.title = title
        self.description = description
        self.status = status

    def mark_completed(self):
        """Отметить задачу как выполненную."""
        self.status = "completed"

    def update_description(self, description: str):
        """Обновить описание задачи."""
        self._validate_description(description)
        self.description = description

    def _validate_description(self, description: str):
        """Проверка длины описания (protected)."""
        if len(description) > 200:
            raise ValueError("Описание задачи слишком длинное.")

    def __str__(self):
        return f"{self.title} - {self.status}"
