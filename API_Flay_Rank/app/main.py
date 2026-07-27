from fastapi import FastAPI
from app.routes import routes_tasks, meta_routes 


app =FastAPI()

app.include_router(routes_tasks.router)
app.include_router(meta_routes.router)
