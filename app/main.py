from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.router import api_router
from app.core.config import settings
from app.core.logging import configure_logging
from app.exceptions import ItemNotFoundError
from app.services.item_service import item_service


def create_app() -> FastAPI:
    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    @application.on_event("startup")
    def startup() -> None:
        configure_logging()
        item_service.reset()

    @application.exception_handler(ItemNotFoundError)
    async def item_not_found_handler(_: Request, exc: ItemNotFoundError) -> JSONResponse:
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    application.include_router(api_router)
    return application


app = create_app()
