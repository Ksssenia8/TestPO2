# tests/test_task.py

import unittest
from src.task import Task

class TestTask(unittest.TestCase):
    def test_mark_completed(self):
        task = Task("Test Task", "Description")
        task.mark_completed()
        self.assertEqual(task.status, "completed")

    def test_update_description(self):
        task = Task("Test Task", "Description")
        task.update_description("New Description")
        self.assertEqual(task.description, "New Description")

    def test_validate_description(self):
        task = Task("Test Task", "Description")
        with self.assertRaises(ValueError):
            task.update_description("A" * 201)
