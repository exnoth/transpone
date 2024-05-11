from uuid import UUID
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_spectacular.utils import extend_schema_view, extend_schema
from transpone_coursework.services.matrix_service import MatrixService
from transpone_coursework.serializers import MatrixSerializer, ResponseMatrixSerializer, UUIDSerializer


class MatrixViewSet(ViewSet):
    m_serv = MatrixService()

    @extend_schema(
        description="Transpose input matrix",
        request=MatrixSerializer,
        responses={
            status.HTTP_422_UNPROCESSABLE_ENTITY: None,
            status.HTTP_200_OK: ResponseMatrixSerializer
        },
        auth=False,
    )
    @action(detail=False, methods=["POST"])
    def post_transpose_matrix(self, request):
        serializer = MatrixSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY, data=serializer.errors
            )

        dto = self.m_serv.transpose(
            serializer.validated_data["matrix"],
        )
        return Response(
            status=status.HTTP_200_OK,
            data=ResponseMatrixSerializer(dto).data,
        )



    @extend_schema(
        description="Get all matrices",
        parameters=[],
        responses={
            status.HTTP_422_UNPROCESSABLE_ENTITY: None,
            status.HTTP_200_OK: MatrixSerializer,
            status.HTTP_404_NOT_FOUND: None,
        },
        auth=False,
    )
    @action(detail=False, methods=["GET"])
    def get_matrix_list(self, _):
        dto = self.m_serv.get_matrices()
        if dto is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(
            status=status.HTTP_200_OK,
            data=ResponseMatrixSerializer(dto, many=True).data,
        )



    @extend_schema(
        description="Get matrix by id",
        parameters=[UUIDSerializer],
        responses={
            status.HTTP_422_UNPROCESSABLE_ENTITY: None,
            status.HTTP_200_OK: ResponseMatrixSerializer,
            status.HTTP_404_NOT_FOUND: None,
        },
        auth=False,
    )
    @action(detail=False, methods=["GET"])
    def get_transpose_matrix(self, request):
        serializer = UUIDSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY, data=serializer.errors
            )

        dto = self.m_serv.find_matrix_by_id(
            serializer.validated_data["id"],
        )
        if dto is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(
            status=status.HTTP_200_OK,
            data=ResponseMatrixSerializer(dto).data,
        )



    @extend_schema(
        description="Delete matrix by id",
        request=UUIDSerializer,
        responses={
            status.HTTP_422_UNPROCESSABLE_ENTITY: None,
            status.HTTP_200_OK: ResponseMatrixSerializer,
            status.HTTP_404_NOT_FOUND: None,
        },
        auth=False,
    )
    @action(detail=False, methods=["POST"])
    def post_delete_matrix(self, request):
        serializer = UUIDSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY, data=serializer.errors
            )

        dto = self.m_serv.delete_matrix_by_id(
            serializer.validated_data["id"],
        )
        if dto is False:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(
            status=status.HTTP_200_OK,
        )
