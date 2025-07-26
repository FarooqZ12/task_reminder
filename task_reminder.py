reminders = []

while True:  # This statement will run the loop. when operation performe.
    print("What do you want to do?")
    print("1. Add a new reminder")
    print("2. View all reminders")
    print("3. Delete a reminder")
    print("4. Exit")

    operation = int(input("What you want? (1,2,3,4) "))  # input from user

    if (operation == 1):  # Add new reminder
        new_reminder = input("Which one you want to add: ")
        reminders.append(new_reminder)
        print("Reminder Added")

    elif (operation == 2):  # print all reminders
        if len(reminders) == 0:
            print("No reminder are added yet! ")
        else:
            for r in reminders:
                print(r)

    elif (operation == 3):  # remove reminder by name or remove complete reminders
        print("1: Remove all reminders")
        print("2: Remove reminder by name")
        rem_choice = input("1 or 2: ")
        if (rem_choice == "1"):
            reminders.clear()
            print("All reminders removed.")
        elif (rem_choice == "2"):
            rem_reminder = input("Which one you want to remove: ")
            if rem_reminder in reminders:
                reminders.remove(rem_reminder)
            else:
                print("This reminder is not in list we have only", reminders)

    elif (operation == 4):  # this will end the the process
        print("Good by")
        break

    else:
        print("Invalid input. Please enter (1,2,3,4): ")
