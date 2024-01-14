from SudokuSolver import SudokuSolver

def main(api_token: str, method: int = 0) -> None:
    solver = SudokuSolver.board_from_preset(api_token=api_token) if (
            method == 0) else SudokuSolver.define_board(api_token=api_token)
    solver.setup()
    solver.start_game()
    solver.tear_down()


if __name__ == '__main__':
    # token ggf. durch neuen ersetzen, username ist standardmäßig auf meinem "Yuutyran" in der Class
    # festgelegt, wäre aber ggf. änderbar
    # method == 0 bedeutet, dass man eine Sudokuboard von presets auswählen kann, 1 bedeutet, dass
    # man sich sein Board selber erstellen kann, aber vorsicht es ist keine Überprüfung vorhanden ob die
    # selber eingetragenden Zahlen valide sind, der Algorithmus funktioniert für invalide Boards ggf. nicht.
    # für method bitte nur 0 oder 1 benutzen.

    method = 1
    token = "API-TOK_sYK0-fsXs-2zCA-9Uke-y1Rk"
    main(api_token=token, method=method)
