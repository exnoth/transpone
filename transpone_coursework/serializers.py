from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers
import numpy as np
from uuid import UUID

class MatrixSerializer(serializers.Serializer):
    matrix = serializers.ListField(
        min_length=2,
        child=serializers.ListField(
            min_length=2,
            child=serializers.FloatField(),
        ),
    )

    def validate_matrix(self, value):
        try:
            matrix = np.array(value)
            if matrix.ndim != 2:
                raise serializers.ValidationError(
                    "Matrix must be two-dimensional array"
                )
        except ValueError:
            raise serializers.ValidationError("Matrix rows must be the same length")
        return value


class UUIDSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)


class ResponseMatrixSerializer(UUIDSerializer, MatrixSerializer):
    pass

