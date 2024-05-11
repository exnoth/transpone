from uuid import UUID
import numpy as np
from transpone_coursework.models import MatrixDTO


class MatrixService:
    matrices: dict[UUID: MatrixDTO]

    def __init__(self):
        self.matrices = {}

    def transpose(self, matrix: list[list[float]]) -> MatrixDTO:
        arr = np.array(matrix)
        result = MatrixDTO(np.transpose(arr).tolist())
        self.matrices[result.id] = result
        return result

    def get_matrices(self) -> list[MatrixDTO]:
        return list(self.matrices.values())

    def find_matrix_by_id(self, id: UUID) -> MatrixDTO | None:
        return self.matrices.get(id)

    def delete_matrix_by_id(self, id: UUID) -> bool:
        result = self.matrices.pop(id, None)
        if result is None:
            return False
        return True
