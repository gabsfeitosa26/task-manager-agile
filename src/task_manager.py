class Task:
    def __init__(self, task_id, title, status="A_FAZER"):
        if not title:
            raise ValueError("O título da tarefa é obrigatório")
        self.id = task_id
        self.title = title
        self.status = status


class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, task_id, title):
        task = Task(task_id, title)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def update_task(self, task_id, new_title):
        for task in self.tasks:
            if task.id == task_id:
                task.title = new_title
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]

    def change_status(self, task_id, new_status):
        for task in self.tasks:
            if task.id == task_id:
                task.status = new_status
                return task
        return None

    # 🔄 Mudança de escopo
    def filter_by_status(self, status):
        return [task for task in self.tasks if task.status == status]
