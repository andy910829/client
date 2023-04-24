from AddStu import AddStu
from PrintAll import PrintAll
from client import SocketClient

action_list = {
    "add": AddStu,
    "show": PrintAll
}

def main():
    host = "127.0.0.1"
    port = 20001
    client = SocketClient(host, port)
    select_result = "initial"

    while select_result != "exit":
        select_result = print_menu()
        try:
            student_list = action_list[select_result]().execute(client)

        except:
            pass
    
def print_menu():
    print()
    print("add: Add a student's name and score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")

    return selection

main()