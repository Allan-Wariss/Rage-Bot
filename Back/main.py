from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.scheduler import schedule_tasks
from app.routes import bot, prompts

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicia o scheduler quando o app inicia
    schedule_tasks()
    yield
    # Limpeza quando o app para

app = FastAPI(lifespan=lifespan)

app.include_router(bot.router, prefix="/api")
app.include_router(prompts.router, prefix="/api/prompts")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)