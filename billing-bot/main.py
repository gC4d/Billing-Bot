from app.api.middlewares.not_found_middleware import NotFoundMiddleware
from app.api.router import router

from fastapi import FastAPI

app = FastAPI(title="Billing Bot API", version="1.0.0")

app.add_middleware(NotFoundMiddleware)

app.include_router(router)