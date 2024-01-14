from boards import *


class InputValidator:
    """
    Helper class for Sudokusolver board input validation.
    Always uses recursive functions to validate input.
    """

    @staticmethod
    def get_and_validate_user_input() -> list[list]:
        user_input = input("Was soll benutzt werden?")
        match user_input:  # user chooses board difficulty for preset boards
            case "Einfach":
                return BOARD_EASY
            case "Medium":
                return BOARD_MEDIUM
            case "Schwer":
                return BOARD_HARD
            case "Experte":
                return BOARD_EXPERT
            case "Master":
                return BOARD_MASTER
            case _:
                print("Bitte Wähle ein Board aus!")
                return InputValidator.get_and_validate_user_input()

    @staticmethod
    def user_board_input() -> tuple[int, int]:  # user creates custom board
        user_input = input("Welche Zelle willst du verändern (1 - 9)? Oder Drücke Enter um zu bestätigen")
        try:
            if user_input == "":
                return 0, 0
            elif int(user_input) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return InputValidator.user_cell_input(int(user_input))
            else:
                print("Wähle eine Valide Zahl")
                return InputValidator.user_board_input()
        except ValueError:
            print("Wähle eine Valide Zahl")
            return InputValidator.user_board_input()

    @staticmethod
    def user_cell_input(cell: int) -> tuple[int, int]:  # user creates custom board
        user_input = input("Welche Zahl soll geändert werden (1 - 9)? Oder Drücke Enter um zurück zu gehen")
        try:
            if user_input == "":
                return InputValidator.user_board_input()
            elif int(user_input) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return cell, int(user_input)
            else:
                print("Wähle eine Valide Zahl")
                return InputValidator.user_cell_input(cell)
        except ValueError:
            print("Wähle eine Valide Zahl")
            return InputValidator.user_cell_input(cell)

    @staticmethod
    def choose_number(allowed_numbers: dict, cell: int, current_number: int) -> int | str:
        # lets user choose a possible number
        print("Welche Zahl soll da sein?")
        numbers = allowed_numbers[str(cell)]
        while True:
            print("Welche Zahl soll da sein?")
            print("Du kannst eine dieser wählen:")
            print(numbers)
            user_input = input("Welche Zahl soll da sein? Oder Drücke Enter um nichts zu ändern")
            try:
                if user_input == "":
                    return current_number
                elif int(user_input) in numbers:
                    return user_input
                else:
                    continue
            except ValueError:
                print("Benutze eine valide Zahl")
