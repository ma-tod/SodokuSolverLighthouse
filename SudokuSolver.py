from time import sleep

from pyghthouse import Pyghthouse

from color_translator import *
from boards import *
from input_validator import InputValidator


class SudokuSolver:

    def __init__(self, board: list[list], username: str = "Yuutyran", api_token: str = ""):
        self.pyghthouse: Pyghthouse = None
        self.board = board
        self.username = username
        self.api_token = api_token

    @classmethod
    def define_board(cls, api_token: str):
        """
        Defines a Sudoku board based on user input and returns it.

        :param api_token: The API token to authenticate the request.
        :return: An instance of the Sudoku class with the defined board.
        """
        allowed_numbers = {"1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           "2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           "3": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           "4": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           "5": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           "6": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           "7": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           "8": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           "9": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}
        board = EMPTY_BOARD
        for i in board:
            print(i)
        edit = True
        while edit:
            cell, number = InputValidator.user_board_input()
            if cell == 0 and number == 0:
                edit = False
            else:
                row = int(((cell - 1) // 3) * 3 + ((number - 1) // 3))
                column = int(((cell - 1) % 3) * 3 + (number - 1) % 3)
                current_number = board[row][column]
                number = InputValidator.choose_number(allowed_numbers, cell, current_number)
                board[row][column] = int(number)
                for i in board:
                    print(i)
        return cls(board, api_token=api_token)


    def __setup_pyghthouse(self) -> None:
        """
        creates a connection to pyghthouse
        """
        self.pyghthouse = Pyghthouse(username=self.username, token=self.api_token)
        self.pyghthouse.start()


    def start_game(self) -> None:
        """solves board"""
        self.solve_board()

    def __get_empty_spot(self) -> tuple[int, int] | bool:
        """
        Tries to find an empty spot in Sudokuboard.

        :return: Either tuple[int, int] (empty spot coordinates) or bool if no spot is found
        """
        row_count = 0
        for row in self.board:
            column_count = 0
            row_count += 1
            for column in row:
                column_count += 1
                if column == 0:
                    return row_count - 1, column_count - 1
        return False

    def __validate_number_for_slot(self, row: int, column: int,
                                   number: int) -> bool:
        """
        Checks if number is valid for the given row and column
        :param row: int row number
        :param column: int column number
        :param number: int number to be validated
        :return: bool True if number is valid, False otherwise
        """
        for x in range(0, 9):
            if self.board[row][x] == number or self.board[x][column] == number:
                return False

            row_of_cell = (row // 3) * 3
            column_of_cell = (column // 3) * 3

            for j in range(row_of_cell, row_of_cell + 3):
                for k in range(column_of_cell, column_of_cell + 3):
                    if self.board[j][k] == number:
                        return False
        return True

    def __setup_color_map(self) -> None:
        """
        Sets up white color outlines for board.
        """
        self.color_map = self.pyghthouse.empty_image()
        for x in range(0, 13, 4):
            for i in range(0, 13):
                self.color_map[x][i] = Color.WHITE.value
                self.color_map[i][x] = Color.WHITE.value

    def solve_board(self) -> bool:
        """
        Recursively solves the board until all cells are valid if a cell isn't valid with all numbers tried
        the number before gets changed
        :return: True if the board was solved, False if there's no solution
        """
        empty_spot = self.__get_empty_spot()
        if not empty_spot:
            return True
        else:
            row, column = empty_spot

        for i in range(1, 10):
            if self.__validate_number_for_slot(row, column, i):
                self.board[row][column] = i

                color_row, color_column = row + 1, column + 1

                if row > 5:
                    color_row += 2
                elif row > 2:
                    color_row += 1

                if column > 5:
                    color_column += 2
                elif column > 2:
                    color_column += 1

                self.color_map[color_row][color_column] = COLOR_TRANSLATOR[str(i)]
                self.pyghthouse.set_image(self.color_map)
                sleep(0.02)

                if self.solve_board():
                    return True

                self.board[row][column] = 0
                self.color_map[color_row][color_column] = Color.BLACK.value
        return False

    @classmethod
    def board_from_preset(cls, api_token: str, arg: str = None):
        """
        Lets user decide what board to use.
        :param api_token: Api token for user authentification
        :param arg: preset in ["Einfach", "Medium", "Schwer", "Experte", "Master"]
        :return: an instance of the SudokuSolver class with preset board
        """
        if arg is not None:
            match arg:
                case "Einfach":
                    return cls(BOARD_EASY, api_token=api_token)
                case "Medium":
                    return cls(BOARD_MEDIUM, api_token=api_token)
                case "Schwer":
                    return cls(BOARD_HARD, api_token=api_token)
                case "Experte":
                    return cls(BOARD_EXPERT, api_token=api_token)
                case "Master":
                    return cls(BOARD_MASTER, api_token=api_token)
                case _:
                    raise Exception
        else:
            print("Welches Feld soll benutzt werden?: ")
            for i in ["Einfach", "Medium", "Schwer", "Experte", "Master"]:
                print(i)
            board = InputValidator.get_and_validate_user_input()
            return cls(board, api_token=api_token)

    def setup(self) -> None:
        """
        Setup color maps and lighthouse connection
        """
        self.__setup_pyghthouse()
        self.__setup_color_map()
        self.__setup_board_color_map()

    def tear_down(self) -> None:
        """
        Resets board colors and lighthouse connection
        """
        self.board = EMPTY_BOARD
        self.__setup_color_map()
        self.pyghthouse.close()
        self.pyghthouse.stop()


    def __setup_board_color_map(self):
        """
        Sets up color maps for existing board
        """
        row_count = 0
        for row in self.board:
            row_count += 1
            column_count = 0
            for column in row:
                column_count += 1
                color_row = row_count
                color_column = column_count
                if row_count > 6:
                    color_row += 2
                elif row_count > 3:
                    color_row += 1
                if column_count > 6:
                    color_column += 2
                elif column_count > 3:
                    color_column += 1
                self.color_map[color_row][color_column] = COLOR_TRANSLATOR[str(column)]

