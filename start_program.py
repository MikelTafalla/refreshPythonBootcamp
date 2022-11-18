from simple_term_menu import TerminalMenu

def option_chosen():
    options = [
        "Get Account Info",
        "Deposit Money",
        "Withdraw Money",
        "Get Balance",
        "Exit"
    ]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]

