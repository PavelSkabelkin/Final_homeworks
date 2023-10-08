class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, task, priority):
        self.tasks.push((task, priority))

    def delete_task(self, task):
        temp_stack = Stack()
        while not self.tasks.is_empty():
            current_task = self.tasks.pop()
            if current_task[0] != task:
                temp_stack.push(current_task)

        while not temp_stack.is_empty():
            self.tasks.push(temp_stack.pop())

    def input_task(self):
        task = input("Введите новую задачу: ")
        priority = int(input("Введите приоритет (целое число): "))
        self.new_task(task, priority)

    def sort_by_priority(self):
        sorted_tasks = sorted(self.tasks.stack, key=lambda x: x[1])
        self.tasks.stack = sorted_tasks

    def __str__(self):
        if self.tasks.is_empty():
            return "No tasks in the manager."

        result = ""
        for task in self.tasks.stack:
            result += f"{task[1]} {task[0]}; "
        return result.rstrip("; ")


# Пример использования:
manager = TaskManager()

while True:
    print("\n1. Ввести новую задачу")
    print("2. Вывести задачи (отсортированные по приоритету)")
    print("3. Удалить задачу")
    print("0. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        manager.input_task()
    elif choice == "2":
        manager.sort_by_priority()
        print(manager)
    elif choice == "3":
        task_to_delete = input("Введите задачу для удаления: ")
        manager.delete_task(task_to_delete)
    elif choice == "0":
        break
    else:
        print("Неверный ввод. Попробуйте еще раз.")
