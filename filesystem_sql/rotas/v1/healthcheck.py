from fastapi import APIRouter

from filesystem_sql.modulos import healthcheck
from filesystem_sql.modelos.healthcheck import HealthcheckResponse, HEALTHCHECK_DEFAULT_RESPONSE

router = APIRouter()


@router.get("/", response_model=HealthcheckResponse, status_code=200, summary="Informa o estado da API",
            responses=HEALTHCHECK_DEFAULT_RESPONSE)
def listar():
    """
    O objetivo do endpoint é informar se a API está no ar, além disso, serve como \
    padrão para os demais endpoints.
    """
    return {"resultado": healthcheck.health_condition()}
