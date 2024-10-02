import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")

        # Frame para la entrada de tareas
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Campo de entrada
        self.task_entry = tk.Entry(self.frame, width=35)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        # Botón para añadir tarea
        self.add_button = tk.Button(self.frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Barra de progreso
        self.progress_label = tk.Label(self.root, text="Tareas Completadas: 0")
        self.progress_label.pack()

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Botón para editar tarea
        self.edit_button = tk.Button(self.root, text="Editar Tarea", command=self.edit_task)
        self.edit_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Botón para restablecer tareas
        self.reset_button = tk.Button(self.root, text="Restablecer Tareas", command=self.reset_tasks)
        self.reset_button.pack(pady=5)

        # Bindings para atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<e>', lambda event: self.edit_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

        self.completed_tasks = 0  # Contador de tareas completadas

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.update_progress()
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(tk.END, task + " - Completada")
            self.completed_tasks += 1
            self.update_progress()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def edit_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            new_task = simpledialog.askstring("Editar Tarea", "Modificar tarea:", initialvalue=task)
            if new_task is not None:
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, new_task)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para editar.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            if " - Completada" in task:
                self.completed_tasks -= 1
            self.task_listbox.delete(selected_task_index)
            self.update_progress()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def reset_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.completed_tasks = 0
        self.update_progress()

    def update_progress(self):
        total_tasks = self.task_listbox.size()
        self.progress_label.config(text=f"Tareas Completadas: {self.completed_tasks}/{total_tasks}")

if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()
