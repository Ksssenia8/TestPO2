# tests/test_task_manager.py

import unittest
from src.task import Task
from src.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.task = Task("Test Task", "Description")

    def test_add_task(self):
        self.manager.add_task(self.task)
        self.assertIn(self.task, self.manager.tasks)

    def test_remove_task(self):
        self.manager.add_task(self.task)
        self.manager.remove_task("Test Task")
        self.assertNotIn(self.task, self.manager.tasks)

    def test_display_tasks(self):
        self.manager.add_task(self.task)
        with self.assertLogs() as log:
            self.manager.display_tasks()
            self.assertIn("Test Task", log.output[0])
