from task_planner import createTaskPlanner, print_dictionaries
# import tkinter as tk
# from tkinter import ttk

planner = createTaskPlanner()

def register_task():
    task = {}
    task['id'] = int(input("Ingrese el ID de la tarea: "))
    task['name'] = input("Ingrese el nombre de la tarea: ")
    task['priority'] = int(input("Ingrese la prioridad de la tarea (entero): "))
    tags_input = input("Ingrese las etiquetas de la tarea (separadas por comas): ")
    task['tags'] = [tag.strip() for tag in tags_input.split(',')]
    planner['addTask'](task)
    print("Tarea registrada exitosamente.")

def mark_task_completed():
    task_name = input("Ingrese el nombre de la tarea a marcar como completada: ")
    planner['markTaskAsCompleted'](task_name)
    print("Tarea marcada como completada.")


while True:
    print("\nMenu:")
    print("1. Registrar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas completadas")
    print("4. Mostrar tareas pendientes")
    print("5. Mostrar tareas ordenadas por prioridad")
    print("6. Filtrar tareas por etiqueta")
    print("7. Mostrar todas las tareas")
    print("8. Remover tarea por ID")
    print("9. Salir")
    
    choice = input("Ingrese el número de opción: ")

    if choice == '1':
        register_task()
    elif choice == '2':
        mark_task_completed()
    elif choice == '3':
        print_dictionaries(planner['getCompletedTasks']())
    elif choice == '4':
        print_dictionaries(planner['getPendingTasks']())
    elif choice == '5':
        print_dictionaries(planner['getSortedTasksByPriority']())
    elif choice == '6':
        tag = input("Ingrese la etiqueta de la tarea para filtrar: ")
        print_dictionaries(planner['filterTasksByTag'](tag)) 
    elif choice == '7':
        print_dictionaries(planner['getTasks']())
    elif choice == '8':
        tag = input("Ingrese el id de la tarea a remover: ")
        planner['removeTask'](tag) 
    elif choice == '9':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida del menú.")

