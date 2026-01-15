import pytest
from src.task_manager import TaskManager

def test_create_task():
    manager = TaskManager()
    task = manager.create_task(1, "Primeira tarefa", priority=2)
    assert task.title == "Primeira tarefa"
    assert task.priority == 2


def test_create_task_without_title():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.create_task(2, "")

def test_change_status():
    manager = TaskManager()
    manager.create_task(1, "Tarefa")
    manager.change_status(1, "EM_PROGRESSO")
    assert manager.tasks[0].status == "EM_PROGRESSO"

def test_filter_by_status():
    manager = TaskManager()
    manager.create_task(1, "Tarefa 1")
    manager.create_task(2, "Tarefa 2")
    manager.change_status(2, "CONCLUIDO")
    result = manager.filter_by_status("CONCLUIDO")
    assert len(result) == 1
