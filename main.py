from operations import *
import os

while True:
    clear_display("File Manager Console")

    print(f'"Current Path: {os.getcwd()}"\n')

    print("1. Create Folder")
    print("2. Create File")
    print("3. Rename")
    print("4. Delete")
    print("5. Display List Directory")
    print("6. Display Info")
    print("7. Change Directory")
    print("8. Back Directory")
    print("0. Exit")

    print('-' * 24)


    try:
        user_selection = int(input("Choose An Operation: "))

        if user_selection < 0:
            raise ValueError

        if user_selection == 1:
            clear_display("CREATE FOLDER")
            create_folder()

        elif user_selection == 2:
            clear_display("CREATE FILE")
            create_file()

        elif user_selection == 3:
            clear_display("RENAME")
            rename_f()

        elif user_selection == 4:
            clear_display("DELETE")
            delete_f()

        elif user_selection == 5:
            clear_display("DISPLAY LIST DIRECTORY")
            list_dir()

        elif user_selection == 6:
            clear_display("DISPLAY INFO")
            show_info_f()

        elif user_selection == 7:
            clear_display("CHANGE DIRECTORY")
            cd()

        elif user_selection == 8:
            clear_display("BACK DIRECTORY")
            back_dir()

        elif user_selection == 0:
            devloper_info()
            break

        else:
            raise ValueError

    except ValueError:
        print("Error in input!\nPlease enter a valid number.")
        input("Press To Continue...")