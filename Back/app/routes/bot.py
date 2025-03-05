from fastapi import APIRouter, Depends
from app.core.bot_engine import BotEngine
from app.core.scheduler import schedule_tasks

router = APIRouter()
bot = BotEngine()

@router.post("/bot/activate")
async def activate_bot():
    schedule_tasks()
    return {"message": "Bot ativado com sucesso"}

@router.post("/bot/post-now")
async def post_manual_tweet():
    success = bot.post_scheduled_tweet()
    return {"success": success, "message": "Tweet postado manualmente"}

@router.get("/bot/status")
async def get_bot_status():
    return {
        "active": True,
        "next_post": "2024-01-01T10:00:00",
        "last_interaction": "2024-01-01T09:30:00"
    }