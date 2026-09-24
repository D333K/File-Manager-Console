import os
import pyfiglet
import termcolor
from datetime import datetime
import json

# =================================

def load_extensions() -> list:
    """This Method Will Load All Extension From JSON File."""

    extension_dir_path = os.path.dirname(__file__)

    extension_json_path = os.path.join(extension_dir_path, "extension.json")

    try:
        with open(extension_json_path, 'r', encoding="utf-8") as extension_file:
            return json.load(extension_file)

    except FileNotFoundError:
        print("Extension File Not Found.")
        return []

    except json.JSONDecodeError:
        print("Error In JSON File.")
        return []

# =================================

def help_user() -> bool:
    """This Method Will Ask User If User Want Help To Choose The Specific Extension."""

    answer = input("Do You Want Help? [y/n]: ").strip().lower()

    if answer == 'n':
        print('-' * 20)
        input("Press To Continue...")
        return False

    elif answer == 'y':
        extensions = load_extensions()

        for index, extension in enumerate(extensions):
            print(f"{index + 1} - {extension}")
        
        print('-' * 20)
        input("Press To Continue...")

    else:
        print("Invalid Answer.")
        print('-' * 20)
        input("Press To Continue...")
        return False

    return True

# =================================

def format_size(size) -> str:
    """This Method  Will Return The Size Od File/Folder In Human Readable Format."""

    for unit in ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0

    return f"{size:.2f} YB"

# =================================

def cal_folder_size(folder_name) -> int:
    """This Method Will Calculate The Size Of Folder."""

    sum_size = 0

    for root, dirs, files in os.walk(folder_name, topdown=False):
        for file in files:
            sum_size += os.path.getsize(os.path.join(root, file))

    return sum_size

# =================================

def del_full_folder(folder_name) -> None:
    """This Method Will Delete Full Folder."""

    for root, dirs, files in os.walk(folder_name, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    os.rmdir(folder_name)

    return

    # =================================

    # Bad Structure💔
    # --------------------------------
    # folders = [folder_name]

    # for root, dirs, files in os.walk(folder_name, topdown=False):
    #     for file in files:
    #         os.remove(file)

    #     folders.append(dirs)

    # back_directory()

    # for index in range(len(folders), 0, -1):
    #     os.rmdir(folders.pop())

    # return

# =================================

def create_folder() -> None:
    """This Method Will Create New Folder."""

    folder_name = input("Enter folder name: ").strip()

    if not folder_name:
        print("Folder Name Can't Be Empty.")
        return

    if os.path.exists(folder_name):
        print("This Folder Is Already Exists.")
        return

    os.mkdir(folder_name)

    print() # New Line. If You Find Like This Line(print()) That's Mean New Line.
    print('-' * 31)
    print("Create Folder Has Successfully.")
    print('-' * 31)
    input("Press To Continue...")
    
    return

# =================================

def create_file() -> None:
    """
        This Method Will Create New File 
        And Ask User About Extension Of File.
    """

    file_name = input("Enter file name: ").strip()

    if not file_name:
        print("File Name Can't Be Empty.")
        return

    extension_type = load_extensions()

    print('-' * 12)
    extension = input("Choose One From This List: ").strip()

    if not extension:
        print("Extension Can't Be Empty.")
        return
    
    flag = False

    for index, exten in enumerate(extension_type): 
            if extension == exten:
                flag = True
                break

    if not flag:
        if not help_user():
            return
        
        return

    # while True:
    #     print('-' * 12)
    #     extension = input("Choose One From This List: ").strip()

    #     if not extension:
    #         print("Extension Can't Be Empty.")
    #         flag = False
        
    #     for index, exten in enumerate(extension_type): 
    #         if extension == exten:
    #             flag = True
    #             break

    #         else:
    #             if index == len(extension_type) - 1:
    #                 print()
    #                 print('-' * 30)
    #                 print("Invalid Extension.")
    #                 print('-' * 30)
    #                 input("Press To Continue...")

    #                 if not help_user():
    #                     flag = False

    #     if not flag:
    #         return

    #     elif flag:
    #         break

    file_name = file_name + '.' + extension

    if os.path.exists(file_name):
        print()
        print('-' * 30)
        print("This File Is Already Exists.")
        print('-' * 30)
        input("Press To Continue...")
        
        return

    with open(file_name, 'w', encoding="utf-8"): 
        print()
        print('-' * 31)
        print("Create File Has Successfully.")
        print('-' * 31)
        input("Press To Continue...")

    return

# =================================

def rename_f() -> None:
    """This Method Will Rename File/Folder."""

    print("NOTE:-\nIf You Want To Rename File " \
                  "Don't Forget To Write File Name And Extension.")
    print('=' * 60)
    print()

    current_name_f = input("Enter the name: ").strip()

    if not current_name_f:
        print("Current Name Can't Be Empty.")
        return

    if os.path.exists(current_name_f):
        new_name_f = input("Enter new name: ").strip()

        if not new_name_f:
            print("New Name Can't Be Empty.")
            return

        os.rename(current_name_f, new_name_f)
        print('-' * 31)
        print(f"{current_name_f} => {new_name_f}")
        print('-' * 31)

        print()
        print('-' * 31)
        print("Rename Has Successfully")
        print('-' * 31)
        input("Press To Continue...")
        
        return

    print()
    print('-' * 39)
    print("There Is No File/Folder With This Name.")
    print('-' * 39)
    input("Press To Continue...")

    return

# =================================

def delete_f() -> None:
    """This Method Will Delete File/Folder."""

    print("NOTE:-\nIf You Want To Delete File " +
                  "Don't Forget To Write File Name And Extension.")
    print('=' * 60)
    print()

    f_name = input("Enter the name: ").strip()

    if not f_name:
        print("File/Folder Name Can't Be Empty.")
        return

    if os.path.isfile(f_name):
        os.remove(os.path.join(os.getcwd(), f_name))

    elif os.path.isdir(f_name):
        answer = input("Are You Sure To Delete This Folder? [y/n]: ").strip().lower()

        if answer == 'y':
            del_full_folder(f_name)

        elif answer == 'n':
            print()
            print('-' * 25)
            input("Press To Continue...")

            return

        else:
            print()
            print('-' * 25)
            print("Invalid Input.")
            print('-' * 25)
            input("Press To Continue...")
            
            return

    else:
        print()
        print('-' * 39)
        print("There Is No File/Folder With This Name.")
        print('-' * 39)
        input("Press To Continue...")
        
        return

    print()
    print('-' * 25)
    print("Delete Has Successfully.")
    print('-' * 25)
    input("Press To Continue...")

    return

# =================================

def list_dir() -> None:
    """This MEthod Will Display All Directory."""

    with os.scandir('.') as files_folders:
        print(f"{'Name':<20} {'Size':<12} {'Last Modified':<20}")
        print('=' * 53)
        print()

        for file_folder in files_folders:
            date_time = datetime.fromtimestamp(os.path.getmtime(file_folder)).strftime("%Y-%m-%d %H:%M:%S")

            if os.path.isfile(file_folder):
                f_size = format_size(os.path.getsize(file_folder))

            elif os.path.isdir(file_folder):
                f_size = format_size(cal_folder_size(file_folder))

            print(f"{file_folder.name:<20} {f_size:<12} {date_time:<20}")

    print()
    print('-' * 20)
    input("Press To Continue...")
    return

# =================================

def show_info_f() -> None:
    """This Method Will Display All Important Information For File/Folder."""

    f_name = input("Enter the name: ").strip()

    if not f_name:
        print("File/Folder Name Can't Be Empty.")
        return

    if os.path.isfile(f_name):
        type = "file"
        f_size = format_size(os.path.getsize(f_name))

    elif os.path.isdir(f_name):
        type = "folder"
        f_size = format_size(cal_folder_size(f_name))

    else:
        print()
        print('-' * 39)
        print("There Is No File/Folder With This Name.")
        print('-' * 39)
        input("Press To Continue...")
        
        return

    date_time = datetime.fromtimestamp(os.path.getmtime(f_name)).strftime("%Y-%m-%d %H:%M:%S")

    print('-' * 39)
    print(f"Name -> {f_name}")
    print(f"Type -> {type}")
    print(f"Size -> {f_size}")
    print(f"Path -> {os.path.abspath(f_name)}")
    print(f"Last Modified -> {date_time}")

    print()
    print('-' * 20)
    input("Press To Continue...")

    return

# =================================

def cd() -> None:
    """This Method Will Change The Current Path."""

    print(f'"Current Path: {os.getcwd()}"\n')

    path = input("Enter full path: ").strip()

    if not path:
        print("Path Can't Be Empty.")
        return

    try:

        if os.path.exists(path):
            os.chdir(path)
            print(f"Path: {os.path.abspath(os.getcwd())}")

            print()
            print('-' * 20)
            input("Press To Continue...")
        
            return
        
    except NotADirectoryError:

        print()
        print('-' * 26)
        print("This Is Not Correct Path.")
        print('-' * 26)
        input("Press To Continue...")

        return

# =================================

def back_dir() -> None:
    """This Method Will Back To The Previous Path."""

    current_path = os.path.abspath(os.getcwd())
    parent_path = os.path.abspath(os.path.join(current_path, os.path.pardir))

    if current_path == parent_path:
        print("You Are In Root Right Now.")
        print()
        print('-' * 20)
        input("Press To Continue...")

    else:
        current_path = current_path.split('/')
        current_path.pop(-1) # To REmove Last Element From List.

        os.chdir(os.path.join('/', *current_path)) # Rewrite The Path To The Previous Path.
        print(f"Path: {os.path.abspath(os.getcwd())}")

        print()
        print('-' * 20)
        input("Press To Continue...")

    return

# =================================

def clear_display(title) -> None:
    """This Method Will Clear The Display And Wait User Until Press Any Key."""

    os.system("cls" if os.name == "nt" else "clear")

    print('=' * 12, end = ' ')
    print(title, end = ' ')
    print('=' * 12, end = "\n\n")

# =================================

def devloper_info() -> None:
    """This Method Will Display Developer Info."""

    os.system("cls" if os.name == "nt" else "clear")
    print(termcolor.colored(pyfiglet.figlet_format("Created By Dark Knight:-"),
                            color="black"))