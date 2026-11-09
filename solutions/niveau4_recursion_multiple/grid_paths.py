"""Solution — grid_paths (niveau 4)."""


def grid_paths(rows: int, cols: int) -> int:
    if rows < 0 or cols < 0:
        raise ValueError("Invalid grid")
    if rows == 0 or cols == 0:          # une seule direction possible : 1 chemin
        return 1
    # le dernier pas est soit vers le bas, soit vers la droite
    return grid_paths(rows - 1, cols) + grid_paths(rows, cols - 1)
