#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 20:02:31 2025

@author: dahiyahhashim
"""

# --------- To Do List ---------
# Prompt: Build a simple, text-based to-do list program that allows users to manage their daily tasks.
# when program runs it should show: 1. Add Task 2. View Task 3. Remove task 4. Exit program
# user can add as many task as they want, viewing tasks should show a numbered list 
# if no tasks exist = print "Your to-do list is empty"
# when removing a task = ask the user 
# handle invalid inputs 
# program should continue running until user chooses to exit option 4 
# BONUS: save tasks to a text file > so list is remembered next time program runs ; add a mark done options that label tasks as [DONE]

import os # for clearing the screen 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def todo_list():
    tasks = [] #store all the tasks in the to do list 
    
    while True:
        print('\n--- To Do List---')
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as DONE")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            clear_screen()
            print("\n--- ADD TASKS ---")
            while True:
                task = input("Enter a new task (or type 'done' to return): ")
                if task.lower() == 'done':
                    break
                tasks.append(task)
                print(f" '{task}' added to your list.")
                
        elif choice == '2':
             clear_screen()
             print('\n--- YOUR TASKS---')
             if not tasks:
                 print("Your to-do list is empty!")
             else:
                 for i, task in enumerate(tasks, start=1):
                     print(f"{i}. {task}")
             input("\nPress Enter to return the menu...")
             
        elif choice == '3':
            clear_screen()
            print("\n--- REMOVE TASKS ---")
            
            if not tasks:
                print("No tasks to remove.")
                input("\nPress Enter to return...")
            else:
                while True:
                    print("\nCurrent Tasks:")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
                        
                    remove_input = input("\nEnter the task number to remove (or type 'done' to return): ")
                    
                    if remove_input.lower() == 'done':
                        break
                    
                    else:
                        try:
                            task_num = int(remove_input)
                            if 1 <= task_num <= len(tasks):
                                removed = tasks.pop(task_num - 1)
                                print(f"Removed: {removed}")
                            else:
                                print("Invalid task number.")
                        except ValueError:
                            print("Please enter a valid number.")
                            
        elif choice == '4':
            clear_screen()
            print("\n--- MARK TASK AS DONE ---")
            
            if not tasks:
                print("No tasks to mark as done.")
                input("\nPlease Enter to return...")
            
            else:
                while True:
                    clear_screen()
                    print("--- MARK TASK AS DONE ---")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
                        
                        # task_num = int(input("\nEnter the task number to mark as done (or type 'done' to return): ")) > turning input into int so 'done' causes a Value error > which is why its saying please enter a valid number
                        
                    task_num = input("\nEnter the task number to mark as done (or type 'done' to return): ")
                    if task_num.lower() == "done":
                        break
                    
                    else:
                        try:
                            task_num = int(task_num)
                            if 1 <= task_num <= len(tasks):
                                if "[DONE]" not in tasks[task_num - 1]:
                                    tasks[task_num - 1] = f"[DONE] {tasks[task_num -1]}"
                                    print("Task mark as done!")
                                else:
                                    print("This task is already marked as done.")
                            else:
                                print("Invalid task number.")
                                
                        except ValueError:
                            print("Please enter a valid number or 'done'.")
                            
                        input("\nPress Enter to continue...")
                        
        elif choice == '5':
            # something is glitching here, doesnt show print statement after certain activities are carried out
            # only shows the print statement if you immediately exit the program
            clear_screen()
            print("Exiting To-Do List. Have a productive day!")
            input("\nPress Enter to close the program...")
            break
        
        else:
            print("Invalid option. Please choose 1–5.")
            input("\nPress Enter to return...")
            
todo_list()
                            
                