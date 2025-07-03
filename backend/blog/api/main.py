from fastapi import FastAPI
from blog.api.routes import user_route
from blog.api.routes import bedroom_route
from blog.api.routes import reservation_route
from blog.api.openapi_tags import openapi_tags


app = FastAPI(
    title="Blog API",
    description="API backend do Blog com Clean Architecture, FastAPI e PostgreSQL",
    version="1.0.0",
    contact={"name": "Lavínia Monteiro", "email": "lavinia@exemplo.com"},
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
    openapi_tags=openapi_tags,
)


@app.get("/")
def ola():
    return {"olá": "fastapi"}


app.include_router(user_route.router, prefix="/users", tags=["Users"])
app.include_router(bedroom_route.router, prefix="/bedrooms", tags=["Bedrooms"])
app.include_router(reservation_route.router, tags=["Reservations"])