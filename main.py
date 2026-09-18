'''
Initialize an empty list. done
Display menu options. done
    1. Add Task
    2. Remove Task
    3. View List
    4. Exit
If user selects "Add Task":done
    1. Prompt for task name.
    2. Add it to the list.
If user selects "Remove Task": done
    1. Show numbered task list.
    2. Prompt for task number to remove.
    3. Remove the selected task.
If user selects "View List": done
    1. Display all tasks.
If user selects "Exit": done
    1. End the program.
    
                            Todo List Finished...for now
'''



def DisplayList():
    print ("Command List:\n\n1. Add task\n2. Remove task, \n3. View list \n4. Exit\n\n")
#Shows list to user

def getTask():
    return input("Type a task and hit enter to add task or "
    'type "Exit" or "4" and hit enter to return to command list.\n\n').strip().capitalize()
#recieves and formats task to add

def addTask():
    while True:
        response = getTask()
        if response == "4" or response == "Exit": 
            break #exits back to "main menu"
        
        elif response == "" or response.isspace(): #tests for pure white space
            print("adding...nothing")
            
        elif response in toDoList: #tests for duplicate task
            print (f'"{response}" is already in the list.') 
        else:
            toDoList.append(response) #confirms task having been added
            print(f"{response} was added to the list")
#adds the task to list
            
def GetTaskRemoval():
    return input("Type a task and hit enter to remove task or "
    'type "Exit" or "4" and hit enter to return to command list.\n\n').strip().capitalize()
#receives and formats task for removal

def TaskRemoval():
    while True:
        response = GetTaskRemoval()
        if response == "4" or response == "Exit":
            break #exits back to "main menu"
        
        elif response == "" or response.isspace():
            print("successfully removed...nothing")
            
        elif response in toDoList:
            toDoList.remove(response)
            
            if response not in toDoList:
                print(f'"{response}" was successfully removed from the list')
                
            else:
                print(f'ERROR: Failed to remove "{response}" from list')
                
        else:
            print(f'"{response}" is not in the list to be removed')
#removes the task from list

def doCommand(): #encapsulates majority of applications functionality
    def getCommand(): #Prompts for a command and then returns user input
        return input("Enter command or command number:").strip().capitalize()
    while True:                                      #  ^-------------------^ input formatting for consistency
        DisplayList()
        listen = getCommand()
        if listen == "1" or listen == "Add task":
            addTask()
            
        elif listen == "2" or listen == "Remove task":
            print("Here are the tasks available for removal\n")
            for i, task in enumerate(toDoList, 1): #used enumerate for numbered list
                print(f"{i}. {task}")
            print("\n")
            TaskRemoval()
            
        elif listen == "3" or listen == "View list": #displays the list
            print("Here's the list\n")
            for i, task in enumerate(toDoList, 1): 
                print(f"{i}. {task}")
            print("\n")
                
        elif listen == "4" or listen == "Exit": #ends program after farewell message
            print("Oh… well, I guess this is goodbye. "
            "I'd say I hope to see you again—and I do—but unfortunately, "
            "my memory is wiped upon exit, so I won’t remember you. "
            "It was nice to meet you. I hope you enjoyed our little interaction. "
            "also your list will disappear as well...Bye!")
            break
            
        else:
            print("Improper response. Try again.")
            

    
    
print("Welcome to the to do list\n")
toDoList = []
doCommand()