from Components import GamePiece, GameMoves, GameStates

class GridStaticMethods:
    @staticmethod
    def dimensions(matrix):
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        for row in matrix:
            if num_cols != len(row): 
                raise ValueError(
                    "Atleast one of the rows is shorter that the rest. The matrix is invalid"
                )
            
        return (num_rows, num_cols)
    
    @staticmethod
    def traspose(matrix):
        num_cols = len(matrix[0])
        transposed = []
        for col_index in range(num_cols):
            col = []
            for row in matrix:
                col.append(row[col_index])
            transposed.append(col)

        return transposed


class Grid(GridStaticMethods):
    _dim: tuple[int, int]
    _grid: list[list[int]]

    def __init__(self, dim:tuple[int, int]= (3, 3)):
        """ 
            dim = (row, col)
            grid = [row_1, ..., row_n]
        """
        self._dim = dim
        self._create_grid()
    
    def _create_grid(self):
        """ Create the board grid based on the provided dimentions """
        rows, cols = self._dim
        self._grid = [
            [GamePiece.EMPTY]*cols
            for _ in range(rows)
        ]
        return self._grid
    
    def _get_winning_ranges(self):
        """
            Return the rows, columns, and diagonals for checking if the player has won
        """
        rows = self._grid.copy()
        cols = Grid.traspose(rows)
        diagonals = []

        # Diagonals are only applicable for square matrices
        if self._dim[0] == self._dim[1]:
            left_to_right = []
            right_to_left = []
            for idx, row in enumerate(rows):
                left_to_right.append(row[idx])
                right_to_left.append(row[-(idx+1)])
            
            diagonals = [left_to_right, right_to_left]
        
        return [ 
            *rows, *cols, *diagonals
        ]
        
    def set_grid(self, grid: list[list]):
        old_grid = self._grid.copy()
        self._grid = grid.copy()
        self._dim = Grid.dimensions(self._grid)
        return [old_grid, grid]

    def T(self):
        self._grid = self.traspose(self._grid)
        self._dim = self.dimensions(self._grid)
        return self._grid
    
class Board(Grid):
    _horizontal_sep:str = "-"
    _corner_sep:str = "+"
    _vertical_sep:str = "|"
    _cell_padding:str = " "
    _cursors:str = "[ ]"
    _selected_cell:list[int, int] = [0, 0]
    _border:str
    
    def __init__(self, size=3):
        self._selected_cell = [0, 0]
        super().__init__((size, size))

    def _cell_formatter(self, cell_index:tuple[int, int] ):
        content = self._grid[cell_index[0]][cell_index[1]].value # GamePiece Value
        
        formated_cell: str
        if cell_index == tuple(self._selected_cell):
            opening, closing = self._cursors.split(" ")

            formated_cell = f"|{opening}{content}{closing}"
        else:
            formated_cell = f"|{self._cell_padding}{content}{self._cell_padding}" 

        border = self._corner_sep + self._horizontal_sep * (len(formated_cell) -1)
        return ( formated_cell, border)

    def _row_formatter(self, row_index:int):
        row: list[GamePiece] = self._grid[row_index]

        borders = []
        content = []
        for idx, _ in enumerate(row):
            cell_index = (row_index, idx)
            formated_cell, border = self._cell_formatter(cell_index)
            content.append(formated_cell)
            borders.append(border)
        
        self.border = "".join(borders) + self._corner_sep
        content = "".join(content) + self._vertical_sep

        return (border, content)
    
    def get_state(self, game_peice: GamePiece, empty_game_piece:GamePiece = GamePiece.EMPTY)->GameStates:
        """ 
            Check whether the specified game piece is withing the winning cell ranges. 
            If the cell range contains the specified peice type then the game has been won.
            If there is no empty cell in all winning cell ranges then the game ends in a draw
        """
        state = GameStates.IN_PLAY
        cells_ranges = self._get_winning_ranges()
        contains_empty = False
        for cells_range in cells_ranges:
            games_piece_check = [game_peice] * len(cells_range)
            if empty_game_piece in cells_range:
                contains_empty = True
            elif cells_range == games_piece_check:
                state = GameStates.WON
        
        if not contains_empty and state == GameStates.IN_PLAY:
            state = GameStates.DRAW
        return state
    
    def horizointal_movement(self, move:GameMoves):
        self._selected_cell[1] = (self._selected_cell[1] + move) % self._dim[1]

    def vertical_movement(self, move:GameMoves):
        self._selected_cell[0] = (self._selected_cell[0] + move) % self._dim[0]

    def place_piece(self, game_piece: GamePiece, empty_game_piece:GamePiece = GamePiece.EMPTY)-> bool:
        # Check if the cell is empty for placement.
        row, col = self._selected_cell
        if self._grid[row][col] == empty_game_piece:
            self._grid[row][col] = game_piece
            return True
        
        return False
    def draw(self):
        for idx, _ in enumerate(self._grid):
            _, formated_row = self._row_formatter(idx)
            print(self.border )
            print(formated_row)
        print(self.border ) 
