from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(
    # title=settings.run.title,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

# main_app.add_middleware(
#     CORSMiddleware,
#     allow_origins=list(settings.run.BACKEND_CORS_ORIGINS),
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
