import numpy as np
from django.db import models
from uuid import UUID, uuid4


class Matrix(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    rows = models.JSONField(null=False)

class MatrixDTO:
    id: UUID
    matrix: list[list[float]]

    def __init__(self, matrix: list[list[float]]):
        self.id = uuid4()
        self.matrix = matrix


