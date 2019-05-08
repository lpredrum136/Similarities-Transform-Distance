from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""

    # Initiate matrix
    matrix = [[0 for x in range(len(b) + 1)] for y in range(len(a) + 1)]

    # Add values to base cases (row 1 and column 1)
    matrix[0][0] = (0, None)
    for i in range(1, len(a) + 1): # Column 1
        matrix[i][0] = (i, Operation.DELETED)
    for j in range(1, len(b) + 1): # Row 1
        matrix[0][j] = (j, Operation.INSERTED)

    # Calculate the rest of the matrix, algorithm from CS50 walkthrough
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):

            # Calculate cost types
            deleteCost = matrix[i - 1][j][0] + 1
            insertCost = matrix[i][j - 1][0] + 1
            if a[i - 1] == b[j - 1]:
                substituteCost = matrix[i - 1][j - 1][0]
            else:
                substituteCost = matrix[i - 1][j - 1][0] + 1

            # Find the smallest cost, also add last operation
            if deleteCost <= insertCost and deleteCost <= substituteCost:
                matrix[i][j] = (deleteCost, Operation.DELETED)
            elif insertCost <= deleteCost and insertCost <= substituteCost:
                matrix[i][j] = (insertCost, Operation.INSERTED)
            else:
                matrix[i][j] = (substituteCost, Operation.SUBSTITUTED)

    # Return
    return matrix