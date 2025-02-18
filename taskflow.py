from datetime import datetime
from typing import List

class Task:
    def __init__(self, title: str, description: str, due_date: str):
        self.title = title
        self.description = description
        self.due_date = self._parse_date(due_date)
        self.completed = False
    
    def _parse_date(self, date_str: str) -> datetime:
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de data inválido. Use AAAA-MM-DD.")
    
    def mark_as_completed(self):
        self.completed = True
    
    def __str__(self):
        status = "Concluída" if self.completed else "Pendente"
        return f"{self.title} - {self.description} (Vence: {self.due_date.strftime('%d/%m/%Y')}) - [{status}]"

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
    
    def add_task(self, title: str, description: str, due_date: str):
        task = Task(title, description, due_date)
        self.tasks.append(task)
    
    def list_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa cadastrada.")
            return
        
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")
    
    def complete_task(self, task_index: int):
        try:
            self.tasks[task_index - 1].mark_as_completed()
            print("Tarefa concluída com sucesso!")
        except IndexError:
            print("Índice inválido! Escolha uma tarefa existente.")
    
    def remove_task(self, task_index: int):
        try:
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Tarefa '{removed_task.title}' removida com sucesso!")
        except IndexError:
            print("Índice inválido! Escolha uma tarefa existente.")

if __name__ == "__main__":
    manager = TaskManager()
    
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            title = input("Título: ")
            description = input("Descrição: ")
            due_date = input("Data de vencimento (AAAA-MM-DD): ")
            try:
                manager.add_task(title, description, due_date)
                print("Tarefa adicionada com sucesso!")
            except ValueError as e:
                print(e)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            manager.list_tasks()
            task_index = int(input("Número da tarefa a concluir: "))
            manager.complete_task(task_index)
        elif choice == "4":
            manager.list_tasks()
            task_index = int(input("Número da tarefa a remover: "))
            manager.remove_task(task_index)
        elif choice == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
